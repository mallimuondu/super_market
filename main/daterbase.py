import sqlite3
conn = sqlite3.connect('conting.db')
c = conn.cursor()
import random
import time
import datetime as time
import sqlite3

def table():
    c.execute('CREATE TABLE IF NOT EXISTS food(total INTEGER)')
table()
def bill_table():
    c.execute('CREATE TABLE IF NOT EXISTS billing( bill INTEGER)')
bill_table()