from flask import Flask, render_template
from flask.ext.pymongo import PyMongo
from flask.ext.pystmark import Pystmark, Message
from pystmark import ResponseError


app = Flask(__name__)
app.config.from_object('config')
mongo = PyMongo(app)
pystmark = Pystmark(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/confirm', methods=['POST'])
def confirm():
    return render_template('confirm.html')


if __name__ == '__main__':
    app.run()
