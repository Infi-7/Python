from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

##CREATE DB
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/infi/Documents/movies.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


##CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

with app.app_context():
    db.create_all()

class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5")
    review = StringField("Your Review")
    submit = SubmitField("Done")

class AddMovieForm(FlaskForm):
    movie_title = StringField("Movie Title")
    submit = SubmitField("Add Movie")

@app.route("/")
def home():
    result = db.session.execute(db.select(Movie))
    all_movies = result.scalars()
    return render_template("index.html", movies=all_movies)

# Adding the Update functionality
@app.route("/edit", methods=["GET", "POST"])
def rate_movie():
    form = RateMovieForm()
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie, form=form)

@app.route("/delete")
def delete():
    movie_id = request.args.get('id')
    movie = db.get_or_404(Movie, movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMovieForm()
    movie_title_request = form.movie_title.data
    if form.validate_on_submit():

        url = "https://api.themoviedb.org/3/search/movie"
        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyZWU3MWYwMzg4NDY0Mjk4NDYzNzZjNjNlNzk5ZjQzOSIsIm5iZiI6MTcyODgxNjUyOC4wMzg0NzEsInN1YiI6IjY3MGJhMjVlYjE1ZDk3YjFhOTNjNzgzNSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.hEJvdYFKfif4jorlB87NVd5RRZ9UavyNxaNpSmj7ScE"
        }

        data = {
            "query":f"{movie_title_request}",
            "include_adult":"True",
        }

        response = requests.get(url, headers=headers, params=data)
        movie_data = response.json()['results']
        return render_template('select.html', data=movie_data)

    return render_template('add.html', form=form)

@app.route('/select')
def select():
    return render_template('select.html')

@app.route('/find')
def find():
    movie_id = request.args.get("id")
    if movie_id:
        url_api_data = f'https://api.themoviedb.org/3/movie/{movie_id}'
        url_image_data = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyZWU3MWYwMzg4NDY0Mjk4NDYzNzZjNjNlNzk5ZjQzOSIsIm5iZiI6MTcyODgxNjY2NS40MTUyNjQsInN1YiI6IjY3MGJhMjVlYjE1ZDk3YjFhOTNjNzgzNSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.k63VWZ9tdC96h7zwkU_uRsTZFDjTj4tYmao0gT5ares"
        }

        response = requests.get(url_api_data,headers=headers).json()
        new_movie = Movie(
            title = response['title'],
            year = response['release_date'].split("-")[0],
            img_url = f"{url_image_data}{response['poster_path']}",
            description = response['overview']
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("home"))



if __name__ == '__main__':
    app.run(debug=True)