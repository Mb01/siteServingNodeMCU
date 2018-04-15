
# prototype web interface


from flask import Flask

app = Flask(__name__)

# somewhere to store our message: a db would be nice
MESSAGE_FILE = "message.txt"


@app.route('/')
def hello_world():
    return 'Hello Flask!'

@app.route('/last-message/')
def last_message():
    message = open(MESSAGE_FILE, "r").read()
    return message

@app.route('/message/<message>')
def message(message):
    open(MESSAGE_FILE, "w").write(message)
    return 'Your message was %s' % message
