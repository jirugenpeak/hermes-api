import sqlite3

def get_tasks():
    con = sqlite3.connect("hermes.db")
    cur = con.cursor()
    output = cur.execute("SELECT * FROM TASKS")
    con.close()
    return output

def create_task(id, title):
    con = sqlite3.connect("hermes.db")
    cur = con.cursor()
    query = (f'insert into TASKS values ({id}, {title}, "OPEN")')
    cur.execute(query)
    con.close()
    return 200

def update_task(id, status):
    con = sqlite3.connect("hermes.db")
    cur = con.cursor()
    query = (f'update TASKS set STATUS = {status} where ID = {id}')
    cur.execute(query)
    con.close()
    return 200

def delete_task(id):
    con = sqlite3.connect("hermes.db")
    cur = con.cursor()
    query = (f'delete from TASKS where ID = {id}')
    cur.execute(query)
    con.close()
    return 200