import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "hermes.db"

def get_tasks():
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    res = cur.execute("SELECT * FROM TASKS")
    rows = res.fetchall()
    con.close()
    return rows

def create_task(task_id, title):
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute("INSERT INTO TASKS VALUES (?, ?, ?)", (task_id, title, "OPEN"))
    con.commit()
    con.close()
    return 200

def update_task(task_id, status):
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute("UPDATE TASKS SET STATUS = ? WHERE TASK_ID = ?", (status, task_id))
    con.commit()
    con.close()
    return 200

def delete_task(task_id):
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute("DELETE FROM TASKS WHERE TASK_ID = ?", (task_id,))
    con.commit()
    con.close()
    return 200
