from flask import *
import requests

URL="https://api.npoint.io/a416bea3bde95c410766"
response = requests.get(URL).json()

app = Flask(__name__)

@app.route("/index.html")
@app.route("/")
def home():
    return render_template("index.html", data=response)

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/contact.html")
def contact():
    return render_template("contact.html")

@app.route("/post/<nums>.html")
def post(nums):
    nums = int(nums)
    return render_template("post.html", data=response, post_id=nums)

if __name__ == "__main__":
    app.run(debug=True)