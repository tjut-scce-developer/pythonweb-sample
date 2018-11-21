#!/usr/bin/python2
# -*- coding: utf-8 -*-


from flask import Flask, render_template, url_for

app = Flask(__name__,  template_folder='templates')

from app import my_route