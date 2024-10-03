from flask import Flask

# custom decorator bolds, emphasises and underlines the output of function
def styler(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return f"<b><em><u>{result}</u></em></b>"
    return wrapper

app = Flask(__name__)

@app.route("/")
@styler
def hello_world():
    return "<p>Hello, World!</p>"

# custom routes
'''
@app.route("/username/<name>")
def greet(name):
    return f"Hello! {name}"
'''

@app.route("/bye")
def bye():
    return "Bye!"

# custom routes with specified data types
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello! {name} you are {number} years old"

if __name__ =="__main__":
    app.run(debug=True)