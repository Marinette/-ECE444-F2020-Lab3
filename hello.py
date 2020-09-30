from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import datetime
app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/user/<name>')
def user(name):
    currentTime = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    return render_template('user.html',name=name, currentDateTime=currentTime)

if __name__ == '__main__':
    app.run(debug=True)
