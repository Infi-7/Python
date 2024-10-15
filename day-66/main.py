from crypt import methods
from xxlimited_35 import error

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, select
import random

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/infi/Documents/cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("index.html")

# HTTP GET - Read Record


@app.route("/random", methods=['GET'])
def get_random_cafes():
    result = db.session.execute(db.select(Cafe)).scalars().all()
    print(len(result))
    output_result = result[random.randint(0,len(result) - 1)]
    cafes = []
    for x in range(1):
        cafe = {"id":f"{output_result.id}",
         "name": f"{output_result.name}",
        "map_url": f"{output_result.map_url}",
        "img_url": f"{output_result.img_url}",
        "location": f"{output_result.location}",
        "seats": f"{output_result.seats}",
        "has_toilet": f"{output_result.has_toilet}",
        "has_wifi": f"{output_result.has_wifi}",
        "has_sockets": f"{output_result.has_sockets}",
        "can_take_calls": f"{output_result.can_take_calls}",
        "coffee_price": f"{output_result.coffee_price}",
         }
        return jsonify({'cafe':cafe})

@app.route("/all", methods=['GET'])
def get_all_cafes():
    result = db.session.execute(db.select(Cafe)).scalars().all()
    cafes = []
    for x in range(len(result)):
        cafe = {"id":f"{result[x].id}",
         "name": f"{result[x].name}",
        "map_url": f"{result[x].map_url}",
        "img_url": f"{result[x].img_url}",
        "location": f"{result[x].location}",
        "seats": f"{result[x].seats}",
        "has_toilet": f"{result[x].has_toilet}",
        "has_wifi": f"{result[x].has_wifi}",
        "has_sockets": f"{result[x].has_sockets}",
        "can_take_calls": f"{result[x].can_take_calls}",
        "coffee_price": f"{result[x].coffee_price}",
         }
        cafes.append(cafe)
    return jsonify({'cafes': cafes})

@app.route('/search/')
def search():
    query_location = request.args.get('loc')
    print(query_location)
    result = db.session.execute(db.select(Cafe).where(Cafe.location == query_location)).scalars().all()
    cafes = []
    if result:
        for x in range(len(result)):
            cafe = {"id": f"{result[x].id}",
                    "name": f"{result[x].name}",
                    "map_url": f"{result[x].map_url}",
                    "img_url": f"{result[x].img_url}",
                    "location": f"{result[x].location}",
                    "seats": f"{result[x].seats}",
                    "has_toilet": f"{result[x].has_toilet}",
                    "has_wifi": f"{result[x].has_wifi}",
                    "has_sockets": f"{result[x].has_sockets}",
                    "can_take_calls": f"{result[x].can_take_calls}",
                    "coffee_price": f"{result[x].coffee_price}",
                    }
            cafes.append(cafe)
        return jsonify({'cafes': cafes})
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404


# HTTP POST - Create Record
@app.route('/add',methods=['POST'])
def add_new_cafe():

    new_cafe = Cafe(
    name = request.form.get('name'),
    map_url = request.form.get('map_url'),
    img_url = request.form.get('img_url'),
    location = request.form.get('location'),
    seats = request.form.get('seats'),
    has_toilet = bool(request.form.get('has_toilet')),
    has_wifi = bool(request.form.get('has_wifi')),
    has_sockets = bool(request.form.get('has_sockets')),
    can_take_calls = bool(request.form.get('can_take_calls')),
    coffee_price = request.form.get('coffee_price'),
    )

    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(responce={"Success": "Successfully added the new cafe."})

# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=['PATCH'])
def update_price(cafe_id):
    new_price = request.args.get('new_price')
    cafe = db.get_or_404(Cafe, cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(responce={"Success": "Successfully change price."}), 200
    else:
        return jsonify(error={"Not Found":"Sorry a cafe with that id was not found in the database."}), 404


# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True, port=5002)
