import dataset

def insert(disname, uid, upassword):

    db = dataset.connect("sqlite:///user.sqlite")
    address = db["userdata"]

    disname = str(disname)
    uid = str(uid)
    upassword = str(upassword)

    

    # address.insert({"name": disname, "id": id, "password": password})
    # address.insert(dict(name = disname, id = uid, password = upassword))

    dict = {}
    dict["name"] = disname
    dict["id"] = uid
    dict["password"] = upassword

    print(dict)

    address.insert(dict)


def searchid(disname):

    db = dataset.connect("sqlite:///user.sqlite")
    address = db["userdata"]

    id = address.find_one(name = disname)
    print(id)

    return id

def searchpass(disname):

    db = dataset.connect("https:///user.sqlite")
    address = db["userdata"]

    password = address.find_one(name = disname)
    print(password)

    return password

"""
def searchurl(disname):

    db = dataset.connect("sqlite:///url.sqlite")
    address = db["url"]

    url = address.find_one()
"""