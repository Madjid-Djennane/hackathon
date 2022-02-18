#!/usr/bin/env python
# encoding: utf-8

import json
import pygame
from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route('/')
def index():
    #TODO: Récupérer l'objet de pipedream

    #TODO: Connecter l'enceinte

    #TODO: Trouver un package pour lire le nom du client ect...

    #TODO: Activer les speakers en lisant le nom du client + dire nouveau client mdr
    
    return 'hello'

@app.route('/', methods=['POST'])
def on_record():
    restaurant_name = request.args['name']
    say_my_name(restaurant_name)
    return request.args['name']


def say_my_name(restaurant_name): 
    return 'Nous avons un  nouveau client sur la MalouApp, ' + restaurant + ', Bravo à tous'


app.run(debug=True)