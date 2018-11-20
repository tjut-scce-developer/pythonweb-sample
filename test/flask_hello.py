#!/usr/bin/python2
# -*- coding: utf-8 -*-

from flask import Flask

first_app = Flask(__name__)


@first_app.route("/")
def hniubi():
    return "这个就没那么牛逼了！"


@first_app.route("/hello/")
def lihaile():
    return "牛逼！"


@first_app.route("/hello/<username>")
def user(username):
    return u" %s 牛逼！" % username


@first_app.route("/hello/<int:no>")
def noniubi(no):
    return u"第 %s 个最牛逼的人！" % no


if __name__ == '__main__':
    first_app.run(debug=True)
