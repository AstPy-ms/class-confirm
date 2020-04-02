import sqlite3

def resetDatabase():
    conn = sqlite3.connect("user.sqlite")
    curs = conn.cursor()
    curs.execute("drop table customer")
    curs.execute("create table customer(name text, username text, password text);")
    for row in curs.execute("select * from customer"):
        print(row)