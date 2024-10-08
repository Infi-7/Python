from flask import *
import requests

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

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
        name = request.form['name']
        email = request.form['email']
        number = request.form['phone']
        message = request.form['message']

        print(f"Name: {name}, email: {email}, number: {number}, message: {message}")

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
