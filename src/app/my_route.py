#!/usr/bin/python2
# -*- coding: utf-8 -*-

from app import app, render_template, url_for
from flask import request

@app.route("/")
@app.route("/index", methods=["GET", "POST"])
def index():
    user = {'username': 'duke'}
    if request.method == "POST":
        user = request.data
    return render_template('index.html', title=u'lichangan', user=user)
