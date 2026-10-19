import sqlite3
conn = sqlite3.connect("tasks.db")

def add_task(title):
    c = conn.cursor()
    c.execute('INSERT INTO tasks (title) VALUES (?)', (title,))
    conn.commit()

def delete_task(task_id):
    c = conn.cursor()
    c.execute('DELETE FROM tasks WHERE id=?', (task_id,))
    conn.commit()

