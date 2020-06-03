# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 12:41:42 2020

@author: laksh
"""

from flask import Flask, request
from backend import *

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])

def parsing():
    body = request.form['Body'].split()
    ticker = body[0]
    action = body[1]
    
    if action == 'quote':
        return ticker_overview(ticker)

if __name__ == "__main__":
    app.run(debug=True)