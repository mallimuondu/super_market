import sqlite3
conn = sqlite3.connect('elployee.db')
c = conn.cursor()
def table():
        c.execute('CREATE TABLE IF NOT EXISTS employee(name TEXT,age INTEGER,salary INTEGER,department TEXT)')
        c.execute('CREATE TABLE IF NOT EXISTS deparmates(depatrarments TEXT)')

table()
def logic():
    a = 'nesh'
    b = 10
    d = 1000
    e = 'department b'
    c.execute('INSERT INTO employee(name,age,salary,department) VALUES(?,?,?,?)',(a,b,d,e))
    conn.commit()
logic()
def add_db():
    add_to_db = c.execute('SELECT * FROM employee WHERE age = 10')
    for name_age in add_to_db:
        with conn:
            print(name_age)
            c.execute('INSERT INTO deparmates(depatrarments) VALUES(?)',(name_age,))
add_db()

def read():
    c.execute('SELECT * FROM deparmates')
    print(c.fetchall())
read()