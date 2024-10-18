from codechef.scraper import scrap_now
from xmlrpc.server import SimpleXMLRPCServer

import os

host = '0.0.0.0'
fallback_port = 10000
if 'PORT' not in os.environ:
    print(f'PORT environment variable not defined.\nUsing fallback port {fallback_port}')
port = int(os.environ.get('PORT', fallback_port))

def serve():
    with SimpleXMLRPCServer((host, port)) as server:
        server.register_introspection_functions()
        funcs = [ scrap_now ]
        for func in funcs:
            server.register_function(func)

        server.serve_forever()

if __name__ == '__main__':
    serve()