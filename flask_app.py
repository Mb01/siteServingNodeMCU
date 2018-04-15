from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Flask!'

@app.route('/last-message/')
def last_message():
    return 'Not implemented yet'

@app.route('/message')
def message():
    return 'Hello Flask!'
