from crypt import methods

from dns.dnssec import validate
from flask import *
from flask_wtf import FlaskForm
from wtforms.fields.simple import EmailField, PasswordField, SubmitField, StringField
from wtforms.validators import DataRequired, Email, Length
from wtforms import *

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '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'

class MyForm(FlaskForm):
    email = StringField('email', [DataRequired(), Email(), Length(min=5)])
    password = StringField('password', [DataRequired(), Length(min=8)])
    submit = SubmitField('Log in')

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET','POST'])
def login():
    login_form = MyForm()
    if login_form.validate_on_submit() and request.method == 'POST':
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template('login.html', form=login_form)

@app.route("/success", methods=['GET','POST'])
def success():
    return render_template('success.html')

@app.route("/denied")
def denied():
    return render_template("denied.html")


if __name__ == '__main__':
    app.run(debug=True)
