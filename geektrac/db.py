import couchdb
from werkzeug.security import check_password_hash, generate_password_hash

from geektrac.util import get_credentials, get_secret



couchserver = None
def start_server(uesrname = None, password = None):
    global couchserver

    if not uesrname or not password:
        username, password = get_credentials()
    
    couchserver = couchdb.Server("http://%s:%s@couchdb:5984/" % (username, password))
    while True:
        try:
            couchserver.version()
            break
        except ConnectionRefusedError:
            pass


dbname = 'users'
dbhandle = None
def get_db_handler():
    global dbhandle
    if couchserver is None:
        start_server()

    if dbhandle is not None:
        return dbhandle
    
    dbhandle = couchserver[dbname]
    return dbhandle

def check_if_user_exists(username):
    if not dbhandle:
        get_db_handler()
    
    if len(dbhandle.view('userdetails/authentication', key = username)) > 0:
        return True
    return False

def check_user_passwd(username, password):
    if not dbhandle:
        get_db_handler()
    
    userEntry = list(dbhandle.view('userdetails/authentication', key = username))
    if len(userEntry) != 1:
        print("Something wrong with database data")
        return False
    
    user = userEntry[0]
    print(user)

    stored_password = user.value.get('password', '')
    if not check_password_hash(stored_password, password):
        return False

    return True

def insert_user_to_db(username, password, email):
    if not dbhandle:
        get_db_handler()
    
    doc = {
        'username': username,
        'password': generate_password_hash(password),
        'email': email,
        'type': 'user/v1'
    }

    dbhandle.save(doc)

    return True

def add_platform_uname_to_db(uname, platform, p_uname):
    if not dbhandle:
        get_db_handler()
    
    user = list(dbhandle.view('userdetails/authentication', key=uname))[0]

    uid = user['id']
    udata = dbhandle[uid]
    if 'platform_uname' not in udata:
        udata['platform_uname'] = dict()
    udata['platform_uname'][platform] = p_uname
    dbhandle[uid] = udata
