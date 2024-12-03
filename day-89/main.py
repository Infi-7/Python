import os
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask import *
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['secret_key']

class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['db_path']
db = SQLAlchemy(model_class=Base)
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)

class User(UserMixin, db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(1000))
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))

with app.app_context():
    db.create_all()

app.route("/index", methods=['GET','POST'])
@app.route("/")
def index():
    return render_template("index.html")

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
                    return redirect(url_for('add'))
                else:
                    error = 'Invalid credentials'
            else:
                error = 'Invalid credentials'
    return render_template("login.html", error=error, logged_in=current_user.is_authenticated)


@app.route("/add",methods=['GET','POST'])
@login_required
def add():
    return render_template("add.html")

if __name__ == "__main__":
    app.run(debug=True, port=5010)