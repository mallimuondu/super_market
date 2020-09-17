import sqlite3
conn = sqlite3.connect('conting.db')
c = conn.cursor()

def table():
    
    c.execute('CREATE TABLE IF NOT EXISTS number(number TEXT)')
    
table()

def insert():
    global a
    a = 1.
    b = int(a)  
    c.execute('INSERT INTO number(number)VALUES(?)',(a,))  
    conn.commit()
insert()
def read():
    for row in c.execute('select * from number'):
        new_list = list(row)
    print(new_list)
    for ele in range(0, len(new_list)): 
        total = a + a 
    print(total)
read()
