#!/bin/python
import sqlite3
from flask import Flask, render_template, request
from sqlite3 import Error

# Flask application object
app = Flask(__name__)

tsks = []

# Home Page 
@app.route('/', methods=['POST', 'GET'])
# @app.route('/index', methods=['POST', 'GET'])
def index():
   if request.method == 'POST':
      new_task = request.form['tsk']
      tsks.append(new_task)
   
   return render_template('index.html', tasks=tsks, page='Home Page')

if __name__ == '__main__':
    app.run(debug=True)
