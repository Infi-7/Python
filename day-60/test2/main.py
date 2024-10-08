from flask import *
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

MY_EMAIL = os.getenv('EMAIL_ID')
MY_PASSWORD = os.getenv('PASS')

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/a416bea3bde95c410766").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET","POST"])
def contact():
    if request.method == 'GET':
        heading  = 'Contact Me'
        return render_template("contact.html", data=heading)
    elif request.method == 'POST':
        heading = 'Successfully sent your message'
        name = str(request.form['name'])
        email = str(request.form['email'])
        number = str(request.form['phone'])
        message = str(request.form['message'])

        MSG = f'Name: {name} \nEmail: {email} \nNumber: {number} \nMessage: {message}'
        print(MSG)

        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=os.getenv('TO_ADDRESS'),
            msg=f"Subject:Details.\n\n{MSG}")

        connection.close()

        return render_template("contact.html", data=heading)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
