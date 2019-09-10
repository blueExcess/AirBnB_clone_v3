#!/usr/bin/python3
""" states view api """

import BaseModel
from flask import Flask, abort, request
from api.v1.views import app_views
import models
import json


@app_views.route('/states', methods=['GET'])
def get_state():
    """ retreive list of states and convert to JSON """
    return json.dumps([state.to_dict()
                       for state in models.storage.all('State')])

@app_views.route('/states/<state_id>', methods=['GET'])
def get_state_id(state_id):
    """ retreive single state matching ID and return in JSON """
    ret =  json.dumps(models.storage.get('State', state_id))
    if get is None:
        abort(404)
    return ret

@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete_state(state_id):
    """ delete state matching given ID. """


@app_views.route('/states', methods=['POST'])
def create_state():
    """ creates a new state object. """


@app_views.route('/states/<state_id>', methods=['PUT'])
def update(state_id):
    """ update specific state object with new information. """


x = request.get_json(silent=True)) #returns body of request as JSON-- if this is none, abort 400
