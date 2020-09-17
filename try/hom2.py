import sqlite3
conn = sqlite3.connect('name_age.db')
c = conn.cursor()

def table():
    
    c.execute('CREATE TABLE IF NOT EXISTS name_age(name TEXT,age INTEGER)')
    
table()
def logic():
    a = 'pizza'10
    c.execute('INSERT INTO name_age(name) VALUES(?,?)',(a,))
logic()
def read():
    c.execute('SELECT * FROM name_age')
    print(c.fetchall())
    conn.commit()
read()