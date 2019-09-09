#!/usr/bin/python3
"""Definition of the API server"""


from api.v1.views import app_views
from flask import Flask
from models import storage
from os import getenv


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def closeStorageAfterRequest(error):
    """Close and reload the storage device between requests"""
    storage.close()
    storage.reload()


if __name__ == '__main__':
    app.run(
        host=getenv('HBNB_API_HOST', '0.0.0.0'),
        port=getenv('HBNB_API_PORT', 5000),
        threaded=True
    )
