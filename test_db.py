import sqlite3
import pytest
from db_logic import add_task, delete_task

@pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (2, 3, 5), (92, 8, 100), (-1000, 999, -1)])

def test_math_params(a, b, expected):
    assert a + b == expected

def test_assert(setup_db):
    add_task("Текст 999")
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    res = c.execute('SELECT * FROM tasks WHERE title = "Текст 999"').fetchall()
    assert res != None
    delete_task(1)

@pytest.fixture()
def setup_db():
    conn = sqlite3.connect('test_tasks.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS tasks
        (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        status INTEGER DEFAULT 0)
    ''')
    yield
    c.execute('''
    DROP TABLE tasks;''')
    conn.commit()
    conn.close()
    print("Hello!")



