from flask import *
from flask_wtf import *
from wtforms import *
from wtforms.validators import *
import mysql.connector

app = Flask(__name__)
app.config['SECRET_KEY'] = 'QYBj6FS58voHmmINudew'

class ContactForm(FlaskForm):
    f_name = StringField('First Name', validators=[DataRequired()])
    l_name = StringField('Last Name', validators=[DataRequired()])
    email = EmailField(validators=[Email()])
    text = TextAreaField()
    submit = SubmitField()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact', methods=['GET','POST'])
def contact():
    contact_form = ContactForm()
    return render_template('contact.html', form=contact_form)

@app.route('/resume')
def resume():
    return render_template('resume.html')

if __name__ == '__main__':
    app.run(debug=True, port=5010)