#!/bin/python
from flask import Flask, render_template, request
from db import *

# Flask application object
app = Flask(__name__)

# tsks = []

# Home Page 
@app.route('/', methods=['POST', 'GET'])
# @app.route('/index', methods=['POST', 'GET'])
def index():
   conn = create_connection('tasks.db')
   if request.method == 'POST':
      new_task = request.form['task']
      new_description = request.form['description']
      create_task(conn, new_task, new_description)

   records = select_all_tasks(conn)
   _tasks = [x[1] for x in records]
   return render_template('index.html', tasks=_tasks, page='Home Page')

if __name__ == '__main__':
    app.run(debug=True)