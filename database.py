#lesson.py
import sqlite3

# create table
# curs.execute("CREATE TABLE customer(name TEXT, username TEXT, password TEXT)")

def searchid(disname):

    # データベースにアクセス
    conn = sqlite3.connect("base2.sqlite")
    curs = conn.cursor()

    disname = str(disname)

    # id = curs.execute("select username from customer where name = ?",[disname])

    for row in curs.execute("select username from customer where name = ?",[disname]):
        print(row)
        id = row


    return id

def searchpass(disname):

    # データベースにアクセス
    conn = sqlite3.connect("base2.sqlite")
    curs = conn.cursor()

    disname = str(disname)

    # password = curs.execute("select password from customer where name = ?", [disname])

    for row in curs.execute("select password from customer where name = ?",[disname]):
        print(row)
        password = row

    return password

def insert(disname, id, password):

    # データベースにアクセス
    conn = sqlite3.connect("base2.sqlite")
    curs = conn.cursor()

    disname = str(disname)
    id = str(id)
    password = str(password)

    print(disname, id, password)

    curs.execute("insert into customer values(?, ?, ?)", [disname, id, password])

    select_sql = 'select * from customer'
    for row in curs.execute(select_sql):
        print(row)

    # curs.execute("drop table customer")
    # curs.execute("CREATE TABLE customer(name text, username text, password text);")

    conn.commit()
    conn.close()