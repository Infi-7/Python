import os
import requests
from dotenv import load_dotenv
from flask import *

load_dotenv()

app = Flask(__name__)

base_url = os.environ['base_url']

@app.route("/", methods=['GET','POST'])
def index():
    response = requests.get(base_url+"/giveaways")
    data = response.json()
    return render_template("index.html", data=data, total=len(response.text))

@app.route("/search_by_id/<int:game_id>", methods=['GET','POST'])
def search_by_id(game_id):
    response = requests.get(base_url+f"/giveaway?id={game_id}")
    data = response.json()
    return render_template("search.html", data=data)

if __name__ == "__main__":
    app.run(debug=True, port=5010)