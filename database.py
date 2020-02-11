#lesson.py
import sqlite3

# create table
# curs.execute("CREATE TABLE customer(name TEXT, username TEXT, password TEXT)")

def searchid(disname):

    # データベースにアクセス
    conn = sqlite3.connect("user.sqlite")
    curs = conn.cursor()

    disname = str(disname)

    # id = curs.execute("select username from customer where name = ?",[disname])

    for row in curs.execute("select username from customer where name = ?",[disname]):
        # print(row)
        id = row

    conn.commit()
    conn.close()

    return id

def searchpass(disname):

    # データベースにアクセス
    conn = sqlite3.connect("user.sqlite")
    curs = conn.cursor()

    disname = str(disname)

    # password = curs.execute("select password from customer where name = ?", [disname])

    for row in curs.execute("select password from customer where name = ?",[disname]):
        # print(row)
        password = row

    conn.commit()
    conn.close()

    return password

def insert(disname, id, password):

    resetDatabase()

    # データベースにアクセス
    conn = sqlite3.connect("user.sqlite")
    curs = conn.cursor()

    disname = str(disname)
    id = str(id)
    password = str(password)

    # print(disname, id, password)

    curs.execute("insert into customer values(?, ?, ?)", [disname, id, password])

    select_sql = 'select * from customer'

    for row in curs.execute(select_sql):
        # print(row)
        pass

    conn.commit()
    conn.close()

'''
    curs.execute("drop table customer")
    curs.execute("create table customer(name text, username text, password text);")

    for row in curs.execute("select * from customer"):
        print(row)
        
'''

def searchurl(disname):

    # データベースにアクセス
    conn = sqlite3.connect("url.sqlite")
    curs = conn.cursor()

    print(disname)

    #curs.execute("drop table customer")
    curs.execute("create table customer(name text, url text);")
    curs.execute("insert into customer values(?, ?)",[disname, "https://discordapp.com/api/webhooks/574167277071761429/mr74pyM_WNR5usMuWZAxf7uX2W10Gv7CS6EsjCQq-uun99mYrdUiM3JVSqKgVwMfFFj7"])

    for row in curs.execute("select * from customer"):
        # print(row)
        pass

    for row in curs.execute("select url from customer where name = ?",[disname]):
        # print(row)
        d = str(row)

    # print(d)

    conn.commit()
    conn.close()

    return d

def resetDatabase():

    conn = sqlite3.connect("user.sqlite")
    curs = conn.cursor()
    curs.execute("drop table customer")
    curs.execute("create table customer(name text, username text, password text);")
    for row in curs.execute("select * from customer"):
        # print(row)
        pass