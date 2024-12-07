import os
import datetime
import time
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
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

    tasks = relationship("Task", back_populates="author")

class Task(db.Model):
    __tablename__ = "tasks"
    id:Mapped[int]=mapped_column(Integer, primary_key=True)
    date:Mapped[str]=mapped_column(String(250), nullable=False)
    tasks:Mapped[str]=mapped_column(String(250), nullable=False)

    author_id:Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id"))
    author:Mapped["User"] = relationship(back_populates="tasks")

with app.app_context():
    db.create_all()

app.route("/index", methods=['GET','POST'])
@app.route("/")
def index():
    return render_template("index.html", logged_in=current_user.is_authenticated)

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
    min_date = datetime.date.today()
    result = db.session.execute(db.select(Task).where((Task.author_id==current_user.id) & (Task.date==min_date))).scalars().all()

    if request.method == 'POST':
        new_task = Task(
            date = request.form.get('date'),
            tasks = request.form.get('task'),
            author = current_user,
        )
        db.session.add(new_task)
        db.session.commit()
        return redirect('add')
    return render_template("add.html", min=min_date, logged_in=current_user.is_authenticated, data=result)

@app.route("/edit/<int:task_id>", methods=['GET', 'POST'])
@login_required
def edit(task_id):
    task_to_edit = db.get_or_404(Task, task_id)

    # Ensure the current user is authorized to edit the task
    if task_to_edit.author_id != current_user.id:
        abort(403)  # Forbidden

    if request.method == 'POST':
        # Update the task
        task_to_edit.date = request.form.get('date')
        task_to_edit.tasks = request.form.get('task')
        db.session.commit()
        flash('Task updated successfully!')
        return redirect(url_for('add'))

    # Render the edit form pre-filled with current task data
    return render_template('edit.html', task=task_to_edit, logged_in=current_user.is_authenticated)


@app.route("/all-tasks", methods=['GET', 'POST'])
@login_required
def all_tasks():
    # Fetch all tasks belonging to the logged-in user
    tasks = db.session.execute(db.select(Task).where(Task.author_id == current_user.id)).scalars().all()

    if request.method == 'POST':
        # Handle editing of tasks directly from this page
        task_id = request.form.get('task_id')
        task_to_edit = db.get_or_404(Task, task_id)

        # Ensure only the owner can edit
        if task_to_edit.author_id != current_user.id:
            abort(403)

        task_to_edit.date = request.form.get('date')
        task_to_edit.tasks = request.form.get('task')
        db.session.commit()
        flash('Task updated successfully!')
        return redirect(url_for('all_tasks'))

    return render_template('all_tasks.html', tasks=tasks, logged_in=current_user.is_authenticated)


@app.route("/delete/<int:task_id>", methods=['GET','POST'])
@login_required
def delete(task_id):
    task_to_delete = db.get_or_404(Task, task_id)
    db.session.delete(task_to_delete)
    db.session.commit()
    time.sleep(2)
    return redirect('/all-tasks')

@app.route('/logout', methods=['GET','POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True, port=5010)