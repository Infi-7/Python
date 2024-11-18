from flask import *
from flask_wtf import *
from wtforms import *
from wtforms.validators import *
import mysql.connector

app = Flask(__name__)
app.config['SECRET_KEY'] = 'QYBj6FS58voHmmINudew'

projects_list = []

class ContactForm(FlaskForm):
    f_name = StringField('First Name', validators=[DataRequired()])
    l_name = StringField('Last Name', validators=[DataRequired()])
    email = EmailField(validators=[Email()])
    text = TextAreaField()
    submit = SubmitField()

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="mydatabase"
)

mycursor = mydb.cursor()
mycursor.execute('select * from projects')
myresult = mycursor.fetchall()

for project in myresult:
  projects_list.append(project)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projects')
def projects():
    inner = []
    outer = []
    count = 0
    len_projects_list = len(projects_list)
    x=3

    for c in range(len_projects_list):
        if count < x:
            inner.append(c)
            count += 1
        elif count == x:
            outer.append(inner)
            inner = []
            inner.append(c)
            count = 1
        if c == len_projects_list - 1 and len(inner) != 0:
            outer.append(inner)
            inner = []

    print(outer)
    return render_template('projects.html', projects=outer,rows = len(outer), project_list = projects_list)

@app.route('/contact', methods=['GET','POST'])
def contact():
    contact_form = ContactForm()
    return render_template('contact.html', form=contact_form)

@app.route('/resume')
def resume():
    return render_template('resume.html')

if __name__ == '__main__':
    app.run(debug=True, port=5010)