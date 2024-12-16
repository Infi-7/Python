import os

import requests
from dotenv import load_dotenv
from flask import *

load_dotenv()
app = Flask(__name__)

base_url = os.environ['base_url']

@app.route("/")
def index():
    response = requests.get(base_url)
    all_products = response.json()
    print(all_products)
    images = []
    for data in all_products:
        images.append(data['image'])
    return render_template("index.html", data=all_products, img_data=images[0:6])

if __name__=="__main__":
    app.run(debug=True, port=5010)