#!/usr/bin/python3
"""The entry point for the API"""


from api.v1.views import app_views


@app_views.route('/status')
def api_status():
    """Report that the API is available"""
    return '{"status": "OK"}'
