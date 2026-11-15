import sqlite3

con = sqlite3.connect("hermes.db")

cur = con.cursor()

cur.execute('''create table if not exists TASKS
            (TASK_ID varchar(5) not null primary key, 
            TASK varchar(100) NOT NULL, 
            STATUS not null check(STATUS not in ('OPEN','CLOSED'))''')

print("database setup completed!")

con.close()