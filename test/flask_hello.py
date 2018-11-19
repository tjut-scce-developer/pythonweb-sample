#!/usr/bin/python2
# -*- coding: utf-8 -*-

from flask import Flask

first_app = Flask(__name__)


@first_app.route("/hello")
def hello_world():
    return "hello world"


if __name__ == '__main__':
    first_app.run()
