from flask import *

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        full_name = str(request.form.get("username"))
        password = str(request.form.get("password"))
        return "Name is "+full_name+" and password is "+password
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)