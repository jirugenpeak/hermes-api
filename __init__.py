import sqlite3
from todos import DB_PATH

def init_db():
    with sqlite3.connect(DB_PATH) as con:
        con.execute('''CREATE TABLE IF NOT EXISTS TASKS
                    (TASK_ID varchar(5) NOT NULL PRIMARY KEY,
                     TASK varchar(100) NOT NULL,
                     STATUS TEXT NOT NULL CHECK (STATUS IN ('OPEN', 'CLOSED')))''')
    print(f"Database setup completed: {DB_PATH}")


if __name__ == "__main__":
    init_db()
