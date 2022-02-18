#!/usr/bin/env python
# encoding: utf-8

import json
from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    #TODO: Récupérer l'objet de pipedream

    #TODO: Connecter l'enceinte

    #TODO: Trouver un package pour lire le nom du client ect...

    #TODO: Activer les speakers en lisant le nom du client + dire nouveau client mdr
    print('lol')
app.run()