#!/usr/bin/python3
"""The entry point for the API"""


from api.v1.views import app_views
import json
import models
import models.base_model


@app_views.route('/status')
def api_status():
    """Report that the API is available"""
    return '{"status": "OK"}'


@app_views.route('/stats')
def api_countModels():
    """Show the counts of each model type in storage"""
    counts = {
        name.lower(): models.storage.count(name)
        for name, cls in models.classes.items()
        if issubclass(cls, models.base_model.Base)
    }
    return json.dumps(counts)
