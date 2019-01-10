#!/bin/python
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import *
from wtforms import *
from db import *

# Flask application object
app = Flask(__name__)

class ToDoForm(Form):
   task = TextField("Task", [validators.DataRequired()])
   description = TextAreaField("Description", [validators.DataRequired()])
   submit = SubmitField("Add")

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
   # _tasks = [x[1] for x in records]
   conn.close()
   return render_template('index.html', tasks=records, page='Home Page', form=ToDoForm())

@app.route('/DeleteTask/<int:id>', methods=['POST'])
def delete_task(id):
   conn = create_connection('tasks.db')
   delete_task_by_id(conn, id)
   conn.close()
   return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)