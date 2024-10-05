from flask import Flask, render_template
import requests

app = Flask(__name__)

url = "https://api.npoint.io/c790b4d5cab58020d391"
response_json = requests.get(url).json()

@app.route('/')
def home():
    return render_template("index.html", posts=response_json)

@app.route("/blog/<nums>")
def get_blog(nums):
    num = int(nums)
    return render_template("post.html", posts=response_json, post_id=num)

if __name__ == "__main__":
    app.run(debug=True)
