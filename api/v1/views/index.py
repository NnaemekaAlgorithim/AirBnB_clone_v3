#!/usr/bin/python3

from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status', methods=['GET'])
def status():
    """Route handler for /status endpoint."""
    return jsonify({"status": "OK"})

if __name__ == "__main__":
    app.run()
