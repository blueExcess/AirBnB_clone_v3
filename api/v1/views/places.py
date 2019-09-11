#!/usr/bin/python3
"""Module for displaying and searching through places for rent"""


from api.v1.views import app_views
import flask
import json
import models


@app_views.route('/places_search', methods=('POST',))
def api_searchPlaces():
    """Search through places"""
    body = flask.request.get_json(silent=True)
    if body is None:
        flask.abort(400)
    places = models.storage.all('Place').values()
    if 'states' in body and len(body['states']) > 0:
        places = [
            place for place in places
            if place.city.state.id in body['states']
        ]
    if 'cities' in body and len(body['cities']) > 0:
        places = [
            place for place in places
            if place.city.id in body['cities']
        ]
    if 'amenities' in body and len(body['amenities']) > 0:
        amenities = set(body['amenities'])
        places = [
            place for place in places
            if amenities - set(am.id for am in place.amenities) == set()
        ]
    return json.dumps([place.to_dict() for place in places])
