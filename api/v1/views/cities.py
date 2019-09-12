#!/usr/bin/python3
""" cities view api routes """

from models.base_model import BaseModel
from flask import Flask, abort, jsonify, request
from api.v1.views import app_views
import models
import json


@app_views.route('/states/<state_id>/cities', methods=['GET'])
def get_city():
    """ return all city objects of a given state. """
    state = models.storage.get('State', state_id)
    if state is None:
        abort(404)
    return jsonify([
        city.to_dict() for city in models.storage.all('City').values()
        ])

# Getting error:
# TypeError: get_city() got an unexpected keyword argument 'state_id'


@app_views.route('/cities/<city_id>', methods=['GET'])
def get_city_id(city_id):
    """ return single city matching id in JSON. """
    city = models.storage.get('City', city_id)
    if city is None:
        abort(404)
    return jsonify(city.to_dict())


@app_views.route('/cities/<city_id>', methods=['DELETE'])
def delete_city(city_id):
    """ delete city matching given id. """
    city = models.storage.get('City', city_id)
    if city is None:
        abort(404)
    city.delete()
    storage.save()
    return jsonify({})
# verify this method works properly


@app_views.route('/states/<state_id>/cities', methods=['POST'])
def create_city(state_id):
    """ create city attached to given state. """
    body = request.get_json(silent=True)
    if body is None:
        abort(400, jsonify(error="Not a JSON"))
    if 'name' not in body:
        abort(400, jsonify(error="Missing name"))
    state = models.storage.get('State', state_id)
    if state is None:
        abort(404)
    city = models.city.City(state_id=state_id, **body)
    models.storage.new(city)
    models.storage.save()
    return jsonify(city.to_dict())


@app_views.route('/cities/<city_id>', methods=['PUT'])
def update_city(city_id):
    """ update specific city object with given information. """
    body = request.get_json(silent=True)
    if body is None:
        abort(400, jsonify("Not a JSON"))
    city = models.storage.get('City', city_id)
    if city is None:
        abort(404)
    for key, value in body.items():
        if key not in ('id', 'state_id', 'created_at', 'updated_at'):
            setattr(city, key, value)
    return jsonify(city.to_dict())
