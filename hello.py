from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required, Email
import datetime

#Object Instantiations
app = Flask(__name__)
app.config['SECRET_KEY'] = 'sdfasd'
bootstrap = Bootstrap(app)
moment = Moment(app)

#Class Declarations
class NameEmailForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    email = StringField('What is your email?', validators=[Email()])
    submit = SubmitField('Submit')

    def NotUTorontoEmail(self,email):
        if email is not None and 'utoronto' in email.lower():
            return False
        return True

#App Routing
@app.route('/',methods=['GET','POST'])
def index():

    name = None
    form = NameEmailForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        old_email = session.get('email')
        email = form.email.data
        #checks
        if old_name is not None and old_name != form.name.data:
            flash("It looks like you've changed your name!")
        if old_email is not None and old_email != form.email.data:
            flash("It looks like you've changed your email!")

        #save info in session
        session['name'] = form.name.data
        session['email'] = form.email.data
        form.name.data = ''
        form.email.data = ''
        return redirect(url_for('index'))

    return render_template('index.html', currentDateTime=datetime.datetime.utcnow(),form=form, name=session.get('name'), email=session.get('email'), InvalidEmail = form.NotUTorontoEmail(session.get('email')))

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
