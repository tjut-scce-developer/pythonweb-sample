#!/usr/bin/python2
# -*- coding: utf-8 -*-


from flask import Flask

app = Flask("lichangan")


@app.route("/")
def index():
    return "index"


@app.route("/login")
def login():
    return "login"


@app.route("/user/<username>")
def user(username):
    return u"user： %s" % username


if __name__ == '__main__':
    app.run(debug=True)
