import os
from flask import Flask
from api.login import app as login_router

CONFIG_FILES = os.path.join('static')

app = Flask(__name__)
app.secret_key = os.urandom(24)

app.register_blueprint(login_router)
  
if __name__ == '__main__':
    app.run(debug = True)
