from flask import *
import mysql.connector

app = Flask(__name__)
app.config['SECRET_KEY'] = 'QYBj6FS58voHmmINudew'

projects_list = []

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
    breaker = 3

    for project_count in range(len_projects_list):
        if count < breaker:
            inner.append(project_count)
            count += 1
        elif count == breaker:
            outer.append(inner)
            inner = []
            inner.append(project_count)
            count = 1
        if project_count == len_projects_list - 1 and len(inner) != 0:
            outer.append(inner)
            inner = []
    return render_template('projects.html', projects=outer,rows = len(outer), project_list = projects_list)

@app.route('/contact', methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        fname = request.form.get('f_name')
        lname = request.form.get('l_name')
        email = str(request.form.get('email'))
        text = str(request.form.get('text'))

        mycursor.execute('select QueryID from userquery order by QueryID desc limit 1')
        myresult_query = mycursor.fetchall()
        print(myresult_query[0][0])
        index = 0
        if myresult_query[0][0] == 0:
            index = 1
        else:
            index = myresult_query[0][0] + 1

        print(index)


        mycursor.execute("INSERT INTO userquery VALUES (%s,%s,%s,%s,%s)", (index, fname, lname, email,text))
        mydb.commit()
        print(index,fname,lname,email,text)
    return render_template('contact.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

if __name__ == '__main__':
    app.run(debug=True, port=5010)