import requests
from flask import *
import random
import datetime


app = Flask(__name__)

@app.route("/")
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now()
    return render_template("index.html", num = random_number, year= current_year.strftime("%Y"))

@app.route("/guess/<name>")
def guesser(name):
    url = f"https://api.genderize.io?name={name}"
    response = requests.get(url).json()

    agify_url = f"https://api.agify.io?name={name}"
    agify_response = requests.get(agify_url).json()

    username = name
    gender = response["gender"]
    age = agify_response["age"]
    return render_template("guesser.html", u_name=username, u_gender=gender, u_age=age)

# Multi value jsons
@app.route("/blog")
def get_blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url).json()

    return render_template("blog.html", posts=response)

if __name__ == "__main__":
    app.run(debug=True)