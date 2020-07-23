# source: https://www.youtube.com/watch?v=o-vsdfCBpsU&list=PLQVvvaa0QuDezJh0sC5CqXLKZTSKU1YNo&index=1

import sqlite3

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()
# uppercases are for sql code understanding
# REAL = float (in python)

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)")

def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(1452549219,'2016-01-11','Python', 6)")
    conn.commit()
    c.close()
    conn.close()

create_table()
data_entry()
