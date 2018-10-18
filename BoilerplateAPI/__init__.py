from flask import Flask
from flask_cors import CORS

from applications import blueprint as api
from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)
CORS(app)
app.wsgi_app = ProxyFix(app.wsgi_app)
app.register_blueprint(api, url_prefix='/api')
