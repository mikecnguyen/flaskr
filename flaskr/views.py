#!/usr/bin/env python
from flaskr import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


@app.errorhandler(404)
def page_not_found(e):
    # This catches all other url's and return index page.
    return render_template('index.html')
