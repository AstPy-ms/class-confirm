#lesson.py
import sqlite3
import subprocess
import gosh

# create table
# curs.execute("CREATE TABLE customer(name TEXT, username TEXT, password TEXT)")

def searchid(disname):

    subprocess.check_call("cat encdata | python3 decrypt.py > user.sqlite", shell=True)
    subprocess.check_call("rm -rf ./encdata", shell=True)

    # データベースにアクセス
    conn = sqlite3.connect("user.sqlite")
    curs = conn.cursor()

    disname = str(disname)

    # id = curs.execute("select username from customer where name = ?",[disname])

    for row in curs.execute("select username from customer where name = ?",[disname]):
        print(row)
        id = row

    conn.commit()
    conn.close()

    subprocess.check_call("cat user.sqlite | python3 encrypt.py > encdata", shell=True)
    subprocess.check_call("rm -rf ./user.sqlite", shell=True)

    return id

def searchpass(disname):

    subprocess.check_call("cat encdata | python3 decrypt.py > user.sqlite", shell=True)
    subprocess.check_call("rm -rf ./encdata", shell=True)

    # データベースにアクセス
    conn = sqlite3.connect("user.sqlite")
    curs = conn.cursor()

    disname = str(disname)

    # password = curs.execute("select password from customer where name = ?", [disname])

    for row in curs.execute("select password from customer where name = ?",[disname]):
        print(row)
        password = row

    conn.commit()
    conn.close()

    subprocess.check_call("cat user.sqlite | python3 encrypt.py > encdata", shell=True)
    subprocess.check_call("rm -rf ./user.sqlite", shell=True)

    return password

def insert(disname, id, password):

    # resetDatabase()

    subprocess.check_call("cat encdata | python3 encrypt.py > user.sqlite", shell=True)
    subprocess.call("rm -rf ./encdata", shell=True)

    # データベースにアクセス
    conn = sqlite3.connect("user.sqlite")
    curs = conn.cursor()

    disname = str(disname)
    id = str(id)
    password = str(password)

    print(disname, id, password)

    curs.execute("insert into customer values(?, ?, ?)", [disname, id, password])

    select_sql = 'select * from customer'

    for row in curs.execute(select_sql):
        print(row)

    conn.commit()
    conn.close()

    subprocess.check_call("cat user.sqlite | python3 encrypt.py > encdata", shell=True)
    subprocess.check_call("rm -rf ./user.sqlite", shell=True)


def searchurl(disname):

    subprocess.check_call("cat encdata | python3 encrypt.py > user.sqlite", shell=True)
    subprocess.check_call("rm -rf ./encdata", shell=True)

    # データベースにアクセス
    conn = sqlite3.connect("url.sqlite")
    curs = conn.cursor()

    print(disname)

    #curs.execute("drop table customer")
    curs.execute("create table customer(name text, url text);")
    curs.execute("insert into customer values(?, ?)",[disname, "https://discordapp.com/api/webhooks/574167277071761429/mr74pyM_WNR5usMuWZAxf7uX2W10Gv7CS6EsjCQq-uun99mYrdUiM3JVSqKgVwMfFFj7"])

    for row in curs.execute("select * from customer"):
        print(row)

    for row in curs.execute("select url from customer where name = ?",[disname]):
        print(row)
        d = str(row)

    # print(d)

    conn.commit()
    conn.close()
    
    subprocess.check_call("cat user.sqlite | python3 encrypt.py > encdata", shell=True)
    subprocess.check_call("rm -rf ./user.sqlite", shell=True)
    
    return d

def resetDatabase():

    conn = sqlite3.connect("user.sqlite")
    curs = conn.cursor()
    curs.execute("drop table customer")
    curs.execute("create table customer(name text, username text, password text);")
    for row in curs.execute("select * from customer"):
        print(row)