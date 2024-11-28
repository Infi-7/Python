from flask import *
import requests

app = Flask(__name__)

@app.route("/")
def index():
    api_request = requests.get("http://127.0.0.1:5002/all")
    cafe_list = api_request.json()
    total_cafes = len(cafe_list["cafes"])

    return render_template("index.html", cafe_list=cafe_list, total=total_cafes)

if __name__ == "__main__":
    app.run(debug=True, port=5010)