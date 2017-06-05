# -*- coding: utf-8 -*-
from flaskr import app
from datetime import datetime
from flask import render_template, request


@app.route('/')
def index():
    keyword = request.values.get('keyword', '')
    if keyword:
        print 'You are searching for {}'.format(keyword)
    else:
        print 'No keyword found.'

    return render_template('index.html', keyword=keyword)


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('/user/login.html')
