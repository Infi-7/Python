import os

from flask import *
import requests
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from dotenv import load_dotenv

# load environment variable
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['secret_key']

class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['db_path']
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE IN DB
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)

class User(UserMixin, db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))

with app.app_context():
    db.create_all()

@app.route("/index", methods=['GET','POST'])
@app.route("/")
def index():
    api_request = requests.get(os.environ['api_link'] + "all")
    cafe_list = api_request.json()
    total_cafes = len(cafe_list["cafes"])

    return render_template("index.html", cafe_list=cafe_list, total=total_cafes, logged_in=current_user.is_authenticated)

@app.route("/signup", methods=['GET','POST'])
def signup():
    error = None
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('email')

        if name and password and email:

            if db.session.execute(db.select(User).where(User.email == email)).scalar() is None:
                hash_and_salted_password = generate_password_hash(
                    request.form.get('password'),
                    method='pbkdf2:sha256',
                    salt_length=8
                )
                new_user = User(
                    email=email,
                    name=name,
                    password=hash_and_salted_password,
                )
                db.session.add(new_user)
                db.session.commit()
                return redirect('login')
            else:
                error = 'Email already exists'
                return redirect('login')
    return render_template("signup.html", error=error, logged_in=current_user.is_authenticated)


@app.route("/login",methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        user_email = request.form.get('email')
        user_password = request.form.get('password')
        if user_email and user_password:
            db_data = db.session.execute(db.select(User).where(User.email==user_email)).scalar()
            if db_data is not None:
                print(db_data)
                if check_password_hash(db_data.password, user_password):
                    session['username'] = db_data.name
                    flash('You were successfully logged in')
                    login_user(db_data)
                    return redirect(url_for('index'))
                else:
                    error = 'Invalid credentials'
            else:
                error = 'Invalid credentials'
    return render_template("login.html", error=error, logged_in=current_user.is_authenticated)


@app.route("/add-cafe",methods=['GET','POST'])
@login_required
def add_cafe():
    if request.method == 'POST':
        payload = {
            'name': request.form.get('name'),
            'map_url': request.form.get('map_url'),
            'img_url': request.form.get('img_url'),
            'location': request.form.get('location'),
            'seats': request.form.get('seats'),
            'has_toilet': bool(request.form.get('has_toilet')),
            'has_wifi': bool(request.form.get('has_wifi')),
            'has_sockets': bool(request.form.get('has_sockets')),
            'can_take_calls': bool(request.form.get('can_take_calls')),
            'coffee_price': request.form.get('coffee_price'),
        }

        response = requests.post(os.environ['api_link'] + "add", data=payload)
        if response.status_code == 200:
            # Redirect to a specific page, e.g., index or success page
            flash("Cafe added successfully!")
            return redirect(url_for('index'))  # Change 'index' to your desired route
        else:
            flash("Failed to add cafe. Please try again.")
            return render_template("add-cafe.html", logged_in=current_user.is_authenticated)
    return render_template("add-cafe.html", logged_in=current_user.is_authenticated)

@app.route('/logout', methods=['GET','POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True, port=5010)