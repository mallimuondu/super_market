import sqlite3
conn = sqlite3.connect('name_age.db')
c = conn.cursor()

def table():
    
    c.execute('CREATE TABLE IF NOT EXISTS name_age(name TEXT,age INTEGER,favoritefood TEXT)')
    
    c.execute('CREATE TABLE IF NOT EXISTS food(fud TEXT)')
    
table()
def logic():
    a = 'nesh'
    b = 10
    d = 'pizza'
    c.execute('INSERT INTO name_age(name,age,favoritefood) VALUES(?,?,?)',(a,b,d))
    conn.commit()
logic()

def add_db():
    age = c.execute('SELECT favoritefood FROM name_age WHERE age = 10')
    for foods in age:
        with conn:
            print(foods)
            c.execute('INSERT INTO food(fud) VALUES(?)',foods)
add_db()

def read():
    c.execute('SELECT * FROM food')
    print(c.fetchall())
read()