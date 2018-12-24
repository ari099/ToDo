import sqlite3, random
from sqlite3 import Error

def create_connection(db_file):
   """
   Create a database connection to the SQLite database
   specified by the db_file
   :param db_file: database file
   :return: Connection object or None
   """
   try:
      conn = sqlite3.connect(db_file)
      return conn
   except Error as e:
      print(e)

   return None


def select_all_tasks(conn):
   """
   Query all rows in the tasks table
   :param conn: the Connection object
   :return:
   """
   cur = conn.cursor()
   cur.execute("SELECT * FROM Tasks")

   rows = cur.fetchall()

   # for row in rows:
   #    print(row)
   return rows


def select_task_by_priority(conn, priority):
   """
   Query tasks by priority
   :param conn: the Connection object
   :param priority:
   :return:
   """
   cur = conn.cursor()
   cur.execute("SELECT * FROM Tasks WHERE priority=?", (priority,))

   rows = cur.fetchall()

   # for row in rows:
   #    print(row)
   return rows

def select_task_by_ID(conn, id):
   """
   Query tasks by ID
   :param conn: the Connection object
   :param id:
   :return:
   """
   cur = conn.cursor()
   cur.execute("SELECT * FROM Tasks WHERE ID=?", (id,))

   rows = cur.fetchall()

   # for row in rows:
   #    print(row)
   return rows


def create_task(conn, task, description):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """
 
    sql = "INSERT INTO Tasks VALUES(?,?,?)"
    cur = conn.cursor()
    cur.execute(sql, (random.randint(1,101), task, description,))
    return cur.lastrowid