import sqlite3

conn = sqlite3.connect("tasks.db")
c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL, 
        status INTEGER DEFAULT 0)
''')
conn.commit()
conn.close()

print("База данных tasks.db и таблица успешно созданы!")