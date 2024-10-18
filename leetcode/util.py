import os

def get_secret(name):
    secret_fpath = f'/run/secrets/{name}'
    existence = os.path.exists(secret_fpath)
    if not existence:
        return None
    with open(secret_fpath) as secret_file:
        secret = secret_file.read().rstrip('\n')
    return secret

def get_credentials():
    user = get_secret('couchdb_uname')
    password = get_secret('couchdb_passwd')

    if not user or not password:
        print("secrets not found")
        exit()
    
    return (user, password)
