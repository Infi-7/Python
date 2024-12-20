import os
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey, Float
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from urllib.parse import urljoin
from dotenv import load_dotenv
import requests
import stripe

# Load environment variables
load_dotenv()

# Validate required environment variables
required_vars = ['secret_key', 'db_path', 'base_url', 'stripe_api_key', 'stripe_webhook_secret']
for var in required_vars:
    if var not in os.environ:
        raise EnvironmentError(f"Missing required environment variable: {var}")

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['secret_key']
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['db_path']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Setup Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, user_id)

# Initialize Stripe
stripe.api_key = os.environ['stripe_api_key']

# User model
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))

    wishlist_items = relationship("Wishlist", back_populates="user")
    cart_items = relationship("Cart", back_populates="user")

# Wishlist model
class Wishlist(db.Model):
    __tablename__ = "wishlist"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    product_id: Mapped[int] = mapped_column(Integer)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))

    user: Mapped["User"] = relationship(back_populates="wishlist_items")

# Cart model
class Cart(db.Model):
    __tablename__ = "cart"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    product_id: Mapped[int] = mapped_column(Integer)
    product_name: Mapped[str] = mapped_column(String(100))
    price: Mapped[float] = mapped_column(Float)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))

    user: Mapped["User"] = relationship(back_populates="cart_items")

# Create database tables
with app.app_context():
    db.create_all()

# Base URL for product API
base_url = os.environ['base_url']

# Routes
@app.route("/")
@app.route("/index", methods=['GET'])
def index():
    try:
        response = requests.get(base_url)
        response.raise_for_status()
        all_products = response.json()
    except requests.RequestException as e:
        flash(f"Error fetching products: {e}", "error")
        all_products = []

    return render_template("index.html", data=all_products, logged_in=current_user.is_authenticated)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_email = request.form.get('email')
        user_password = request.form.get('password')
        user = User.query.filter_by(email=user_email).first()
        if user and check_password_hash(user.password, user_password):
            login_user(user)
            flash('Logged in successfully!', 'success')
            return redirect(url_for('index'))
        flash('Invalid email or password', 'error')
    return render_template("login.html", logged_in=current_user.is_authenticated)

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        if User.query.filter_by(email=email).first():
            flash("Email already exists", "error")
        else:
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
            new_user = User(name=name, email=email, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            flash("Account created successfully!", "success")
            return redirect(url_for('login'))
    return render_template("signup.html", logged_in=current_user.is_authenticated)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out successfully", "success")
    return redirect(url_for('index'))

@app.route("/product-details/<int:product_id>")
def product_details(product_id):
    response = requests.get(base_url+f"/{product_id}")
    data = response.json()
    return render_template("product.html", data=data)

@app.route("/wishlist", methods=["GET"])
@login_required
def display_wishlist():
    wishlist_items = Wishlist.query.filter_by(user_id=current_user.id).all()
    product_details = []

    # Fetch product details from the API for each product in the wishlist
    for item in wishlist_items:
        try:
            product_url = urljoin(base_url, f"{item.product_id}")
            response = requests.get(product_url)
            response.raise_for_status()
            product = response.json()
            product_details.append({
                'id': item.product_id,
                'name': product.get('name', 'Unknown Product'),
                'price': product.get('price', 0.0),
                'image': product.get('image', '/static/default.jpg')
            })
        except requests.RequestException as e:
            product_details.append({
                'id': item.product_id,
                'name': 'Unknown Product',
                'price': 0.0,
                'image': '/static/default.jpg'
            })

    return render_template("wishlist.html", products=product_details, logged_in=current_user.is_authenticated)

@app.route("/wishlist/add/<int:product_id>")
@login_required
def add_to_wishlist(product_id):
    if not Wishlist.query.filter_by(user_id=current_user.id, product_id=product_id).first():
        db.session.add(Wishlist(user_id=current_user.id, product_id=product_id))
        db.session.commit()
        flash("Product added to wishlist", "success")
    else:
        flash("Product already in wishlist", "info")
    return redirect(url_for('index'))

@app.route("/wishlist/remove/<int:product_id>")
@login_required
def remove_from_wishlist(product_id):
    item = Wishlist.query.filter_by(user_id=current_user.id, product_id=product_id).first()
    if item:
        db.session.delete(item)
        db.session.commit()
        flash("Product removed from wishlist", "success")
    else:
        flash("Product not found in wishlist", "error")
    return redirect(url_for('index'))

@app.route("/cart/add/<int:product_id>")
@login_required
def add_to_cart(product_id):
    try:
        response = requests.get(urljoin(base_url, f"{product_id}"))
        response.raise_for_status()
        product = response.json()

        if not Cart.query.filter_by(user_id=current_user.id, product_id=product_id).first():
            db.session.add(Cart(
                user_id=current_user.id,
                product_id=product_id,
                product_name=product.get('name', 'Unknown Product'),
                price=product.get('price', 0.0)
            ))
            db.session.commit()
            flash("Product added to cart", "success")
        else:
            flash("Product already in cart", "info")
    except requests.RequestException as e:
        flash(f"Error adding product to cart: {e}", "error")
    return redirect(url_for('index'))

@app.route("/cart/remove/<int:product_id>", methods=["GET"])
@login_required
def remove_from_cart(product_id):
    item = Cart.query.filter_by(user_id=current_user.id, product_id=product_id).first()
    if item:
        db.session.delete(item)
        db.session.commit()
        flash("Product removed from cart", "success")
    else:
        flash("Product not found in cart", "error")
    return redirect(url_for('display_cart'))

@app.route("/cart", methods=["GET"])
@login_required
def display_cart():
    cart_items = Cart.query.filter_by(user_id=current_user.id).all()
    total_price = sum(item.price for item in cart_items)

    return render_template("cart.html", cart_items=cart_items, total_price=total_price, logged_in=current_user.is_authenticated)

@app.route("/cart/checkout")
@login_required
def checkout():
    cart_items = Cart.query.filter_by(user_id=current_user.id).all()
    if not cart_items:
        flash("Your cart is empty", "info")
        return redirect(url_for('index'))

    try:
        stripe_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {'name': item.product_name},
                        'unit_amount': int(item.price * 100),
                    },
                    'quantity': 1,
                }
                for item in cart_items
            ],
            mode='payment',
            success_url=url_for('checkout_success', _external=True),
            cancel_url=url_for('index', _external=True),
        )
        return redirect(stripe_session.url)
    except stripe.error.StripeError as e:
        flash(f"Stripe error: {e}", "error")
    return redirect(url_for('index'))

@app.route("/checkout/success")
@login_required
def checkout_success():
    Cart.query.filter_by(user_id=current_user.id).delete()
    db.session.commit()
    flash("Payment successful! Your cart is now empty.", "success")
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True, port=5010)
