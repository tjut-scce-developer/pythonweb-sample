#!/usr/bin/python2
# -*- coding: utf-8 -*-


from flask import render_template, Flask, url_for

app = Flask(__name__)


@app.route("/")
@app.route("/login/<name>")
def login(name=None):
    return render_template('login.html', name=name)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)
    # main()

