from flask import Flask

import os

from geektrac.util import get_secret

host = '0.0.0.0'
fallback_port = 5000
if 'PORT' not in os.environ:
    print(f'PORT environment variable not defined.\nUsing fallback port {fallback_port}')
port = int(os.environ.get('PORT', fallback_port))

def create_app():
    app = Flask(__name__)
    from geektrac.views import user_creation, user_detail
    app.register_blueprint(user_creation)
    app.register_blueprint(user_detail)

    app.config['SECRET_KEY'] = get_secret('secret_key')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host = host, port = port)