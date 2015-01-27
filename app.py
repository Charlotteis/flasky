from flask import Flask, request
from flask.ext.script import Manager
app = Flask(__name__)
manager = Manager(app)


@app.route("/")
def index():
    user_agent = request.headers.get("User-Agent")
    return "<p>Your browser is {0}<p>".format(user_agent)


@app.route("/user/<name>")
def user(name):
    name = name.capitalize()
    return "<h1>Hello, {0}</h1>".format(name)


if __name__ == "__main__":
    manager.run()
