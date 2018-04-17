
# prototype web interface


from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from _my_secrets import SQLALCHEMY_DATABASE_URI

app = Flask(__name__)
app.config["DEBUG"] = True


app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)

class Comment(db.Model):

    __tablename__ = "comments"

    id      = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))

class Message(db.Model):
    __tablename__ = "messages"

    id      = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("main_page.html", comments=Comment.query.all())
    #POST
    # grab the contents of the form when posting
    comment = Comment(content=request.form["contents"])
    db.session.add(comment)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/interface', methods=["GET", "POST"])
def interface():
    if request.method == "GET":
        return render_template("main_page.html", comments=Message.query.all())
    #POST
    # grab the contents of the form when posting
    message = Message(content=request.form["message"])
    db.session.add(message)
    db.session.commit()
    return redirect(url_for('interface'))
