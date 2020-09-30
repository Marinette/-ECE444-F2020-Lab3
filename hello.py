from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment

import datetime
app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def index():
    return render_template('index.html', currentDateTime=datetime.datetime.utcnow())
@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name, currentDateTime=datetime.datetime.utcnow())

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html',currentDateTime=datetime.datetime.utcnow()), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html',currentDateTime=datetime.datetime.utcnow()), 500

if __name__ == '__main__':
    app.run(debug=True)
