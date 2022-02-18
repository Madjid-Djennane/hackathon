#!/usr/bin/env python
# encoding: utf-8

import json
import pygame
from flask import Flask, request, jsonify
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
import sys
import subprocess
from tempfile import gettempdir
from dotenv import load_dotenv

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
    # Create a client using the credentials and region defined in the [adminuser]
    # section of the AWS credentials file (~/.aws/credentials).
    session = Session(profile_name="adminuser")
    polly = session.client("polly")

    try:
        # Request speech synthesis
        response = polly.synthesize_speech(Text=say_my_name(restaurant_name), OutputFormat="mp3",
                                            VoiceId="Joanna")
    except (BotoCoreError, ClientError) as error:
        # The service returned an error, exit gracefully
        print(error)
        sys.exit(-1)


def say_my_name(restaurant_name): 
    return 'Nous avons un  nouveau client sur la MalouApp, ' + restaurant_name + ', Bravo à tous'


app.run(debug=True)