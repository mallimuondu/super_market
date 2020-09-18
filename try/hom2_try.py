import sqlite3
conn = sqlite3.connect('name_age_try.db')
c = conn.cursor()

def table():
    
    c.execute('CREATE TABLE IF NOT EXISTS name_age(Brand TEXT,price INTEGER)')
    
table()
def insert():
    with conn:
        c.execute('INSERT INTO name_age VALUES("Toyota",1000)')
insert()
def read():
    c.execute('SELECT * FROM name_age')
    print(c.fetchall())
read()
def add_acc():
    brand = c.execute('SELECT * FROM name_age WHERE price = 1000')
    for car in brand:
        print(car)
add_acc()