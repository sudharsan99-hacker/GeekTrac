import os
import jwt
from datetime import date,datetime

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


from functools import wraps
from flask import current_app
from flask import request, abort

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
                token = request.headers.get("Authorization")
        if not token:
            return {
                "message": "Authentication Token is missing!",
                "data": None,
                "error": "Unauthorized"
            }, 401
        try:
            token_data = jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
            if 'valid_till' not in token_data:
                raise Exception("token invalid")
            expiry_time = datetime.strptime( token_data['valid_till'], "%Y-%m-%d %H:%M:%S.%f")
            if datetime.now() >= expiry_time:
                raise Exception("token expired")
        except Exception as e:
            return {
                "message": "Something went wrong",
                "data": None,
                "error": str(e)
            }, 403
        
        return f(token_data, *args, **kwargs)
    
    return decorated

from xmlrpc.client import Server
leetcode_handle = None
codechef_handle = None

def get_leetcode_handle():
    global leetcode_handle
    
    leetcode_handle = Server('http://leetcode:1006/')
    return leetcode_handle
    # while True:
    #     try:
    #         couchserver.version()
    #         break
    #     except ConnectionRefusedError:
    #         pass

def get_codechef_handle():
    global codechef_handle
    
    codechef_handle = Server('http://codechef:1006/')
    return codechef_handle
    # while True:
    #     try:
    #         couchserver.version()
    #         break
    #     except ConnectionRefusedError:
    #         pass
