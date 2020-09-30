from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
import datetime

#Object Instantiations
app = Flask(__name__)
app.config['SECRET_KEY'] = 'roccoladocco253'
bootstrap = Bootstrap(app)
moment = Moment(app)

#Class Declarations
class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')

#App Routing
@app.route('/',methods=['GET','POST'])
def index():

    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''

    return render_template('index.html', currentDateTime=datetime.datetime.utcnow(),form=form, name=name)
    
@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name, currentDateTime=datetime.datetime.utcnow())

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html',currentDateTime=datetime.datetime.utcnow()), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html',currentDateTime=datetime.datetime.utcnow()), 500

#main
if __name__ == '__main__':
    app.run(debug=True)
