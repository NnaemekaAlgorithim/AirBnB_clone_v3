#!/usr/bin/python3

from api.v1.views import app_views
from flask import Flask
from models import storage
import os


"""creating an instance of the class Flask and assign it to the variable app"""
app = Flask(__name__)

"""Register the app_views blueprint"""
app.register_blueprint(app_views, url_prefix='/api/v1')

@app.teardown_appcontext
def teardown_appcontext(exception):
    """Method to handle teardown of Flask app context."""
    storage.close()

if __name__ == "__main__":
    host = os.environ.get('HBNB_API_HOST', '0.0.0.0')
    port = int(os.environ.get('HBNB_API_PORT', 5000))

    app.run(host=host, port=port, threaded=True)
