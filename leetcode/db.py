import couchdb

from leetcode.util import get_credentials, get_secret



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


def save_stat(username, userstat):
    if not dbhandle:
        get_db_handler()
    
    stats = list(dbhandle.view('userdetails/leetcode', key = username))

    if len(stats) > 0:
        prev_stat = stats[0]['value']
        prev_stat.update( userstat )
        userstat = prev_stat
        dbhandle[userstat['_id']] = userstat
    else:
        stat = dict()
        stat.update(userstat)
        stat['username'] = username
        stat['type'] = 'stat/leetcode/v1'
        dbhandle.save(stat)

    return True


platform = 'leetcode'
def user_to_platform_uname(user):
    if not dbhandle:
        get_db_handler()

    p_uname = list(dbhandle.view('userdetails/platform_uname', key = user))

    if (len(p_uname) <= 0):
        return ""
    
    p_uname = p_uname[0]['value']
    if not p_uname:
        return ""
        
    return p_uname.get(platform, "")