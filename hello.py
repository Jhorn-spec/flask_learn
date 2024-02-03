from flask import Flask
app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello World! How are you doing.....?"

@app.route('/foobar')
def foobar():
    return '<h1>Hi there, foobar!</h1>'