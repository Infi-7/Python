from crypt import methods

from dns.dnssec import validate
from flask import *
from flask_wtf import FlaskForm
from wtforms.fields.simple import EmailField, PasswordField, SubmitField, StringField
from wtforms.validators import DataRequired
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

class MyForm(FlaskForm):
    email = StringField('email', [
        validators.Length(min=6, message='Little short for an email address?'),
        validators.Email()
    ])
    password = PasswordField('password', [validators.Length(min=8, message="Must be at least 8 characters.")])
    submit = SubmitField('Submit')


app = Flask(__name__)
app.config['SECRET_KEY'] = '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'


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET','POST'])
def login():
    form = MyForm()
    form.validate_on_submit()
    return render_template('login.html', form=form)

@app.route("/success", methods=['GET','POST'])
def success():
    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True)
