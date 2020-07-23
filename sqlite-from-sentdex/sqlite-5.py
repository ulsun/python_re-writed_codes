# kaynak: https://www.youtube.com/watch?v=o-vsdfCBpsU&list=PLQVvvaa0QuDezJh0sC5CqXLKZTSKU1YNo&index=1
import sqlite3
import time
import datetime
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style
style.use('fivethirtyeight')

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)")

def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(1452549219,'2016-01-11 13:53:39','Python', 6)")
    conn.commit()
    #c.close()
    #conn.close()

def dynamic_data_entry():
    unix = int(time.time())
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python' 
    value = random.randrange(0,10)
    c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)",(unix, date, keyword, value))
    conn.commit()


def read_from_db():
    c.execute('SELECT keyword,unix FROM stuffToPlot WHERE unix>1595439082.0')

    #data = c.fetchall()
    #print(data)
    for row in c.fetchall():
        print(row)
    
def graph_data():
    c.execute('SELECT unix, value FROM stuffToPlot')
    dates = []
    values = []
    for row in c.fetchall():
        #print(row[0])
        #print(datetime.datetime.fromtimestamp(row[0]))
        #dates.append()
        dates.append(datetime.datetime.fromtimestamp(row[0]))
        values.append(row[1])
    plt.plot_date(dates, values, '-')
    plt.show()

def del_and_update():
    c.execute('SELECT * FROM stuffToPlot')
    [print(row) for row in c.fetchall()]

    # c.execute('UPDATE stuffToPlot SET value = 99 WHERE value=8')
    # conn.commit()

    # c.execute('SELECT * FROM stuffToPlot')
    # [print(row) for row in c.fetchall()]

    # c.execute('DELETE FROM stuffToPlot WHERE value= 99')
    # conn.commit()
    print(50*"#")

    # c.execute('SELECT * FROM stuffToPlot')
    # [print(row) for row in c.fetchall()]

    c.execute('SELECT * FROM stuffToPlot WHERE value= 2')
    [print(row) for row in c.fetchall()]

    print(50*"#")
    c.execute('SELECT * FROM stuffToPlot WHERE value= 2')
    print(len(c.fetchall()))
    
    print(50*"#")




#create_table()
# data_entry()
# for i in range(10):
#     dynamic_data_entry()
#     time.sleep(1)
#read_from_db()
#graph_data()
del_and_update()

c.close
conn.close()
