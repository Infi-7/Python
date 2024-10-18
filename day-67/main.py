from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
import datetime

'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

app = Flask(__name__)
ckeditor = CKEditor(app)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/infi/Documents/posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()

class MakePostForm(FlaskForm):
    title = StringField('Blog Post Title', validators=[DataRequired()])
    subtitle = StringField('Subtitle', validators=[DataRequired()])
    author = StringField('Your Name', validators=[DataRequired()])
    img_url = StringField('Blog Image URL', validators=[DataRequired()])
    body = CKEditorField('Blog Content', validators=[DataRequired()])
    submit = SubmitField("Submit Post")


@app.route('/',methods=['GET'])
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    if request.method == 'GET':
        all_values = db.session.execute(db.select(BlogPost)).scalars().all()
        posts = []
        for detail in range(len(all_values)):
            entry = [all_values[detail].id, all_values[detail].title,all_values[detail].subtitle,all_values[detail].date,all_values[detail].body,all_values[detail].author,all_values[detail].img_url]
            posts.append(entry)
        return render_template("index.html", all_posts=posts)

# TODO: Add a route so that you can click on individual posts.
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    requested_post = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalars().all()
    print(requested_post)
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route('/new-post', methods=['GET', 'POST'])
def new_post():
    form = MakePostForm()
    heading = "New Post"
    if request.method == 'POST':
        new_post = BlogPost(
            title=request.form.get('title'),
            subtitle=request.form.get('subtitle'),
            author=request.form.get('author'),
            img_url=request.form.get('img_url'),
            body=request.form.get("body"),
            date=datetime.datetime.now().strftime("%B %d, %Y")
        )

        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))

    return render_template('make-post.html', form=form, post_heading=heading)

# TODO: edit_post() to change an existing blog post
@app.route('/edit/<int:post_id>', methods=['GET','POST'])
def edit(post_id):
    post = db.get_or_404(BlogPost, post_id)
    form = MakePostForm(title=post.title,
                        subtitle=post.subtitle,
                        img_url=post.img_url,
                        author=post.author,
                        body=post.body,
                        )
    if request.method == "POST":
        if form.validate_on_submit():
            post.title = form.title.data
            post.subtitle = form.subtitle.data
            post.img_url = form.img_url.data
            post.author = form.author.data
            post.body = form.body.data

            db.session.commit()
            return redirect(url_for('show_post', post_id=post.id))

    heading = "Edit Post"
    return render_template('make-post.html', form=form, post=post, post_heading=heading, post_id=post.id)

# TODO: delete_post() to remove a blog post from the database
@app.route('/delete')
def delete():
    pass

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
