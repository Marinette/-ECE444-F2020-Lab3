from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required, Email
import datetime
from flask_sqlalchemy import SQLAlchemy
import os
from flask.ext.script import Shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)
manager.add_command("shell", Shell(make_context=make_shell_context))

#Object Instantiations
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = 'asdsafg'
app.config['SQLALCHEMY_DATABASE_URI'] =\
'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)


#Class Declarations
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role',lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username

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
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
        else:
            session['known'] = True

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

    return render_template('index.html', currentDateTime=datetime.datetime.utcnow(),
    form=form, name=session.get('name'), email=session.get('email'),
    InvalidEmail = form.NotUTorontoEmail(session.get('email')),
    known=session.get('known',False))

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
