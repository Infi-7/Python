from flask import *
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = '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'

class Myform(FlaskForm):
    name = StringField('name', validators=[DataRequired(message="Input required!")])

@app.route('/', methods=['GET', 'POST'])
def home():
    login_form = Myform()
    if login_form.validate_on_submit():
        return redirect('/success')

    return render_template('index.html', form=login_form)

@app.route('/success')
def success():
    return render_template('success.html')



if __name__ == "__main__":
    app.run(debug=True)

