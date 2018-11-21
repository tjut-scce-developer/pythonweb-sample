#!/usr/bin/python2
# -*- coding: utf-8 -*-


from flask import Flask, url_for, request

app = Flask("lichangan")


@app.route("/")
@app.route("/index")
def index():
    return "index"


@app.route("/login", methods=["GET", "POST"])
def login():
    return "login"


@app.route("/user/<username>")
def user(username):
    return u"user： %s" % username


def main():
    with app.test_request_context():
        print url_for('index')
        print url_for('login')
        print url_for('login', next='lichangan')
        print url_for('user')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)
    # main()

