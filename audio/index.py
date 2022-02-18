import pygame
import os
import requests
import random
import string


def play_song():
    pygame.mixer.init()
    pygame.mixer.music.load("song.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

def play_multiplex():
    pygame.mixer.init()
    pygame.mixer.music.load("multiplex.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

def play_remote_media(url):
    # download media
    media_path = download_media(url)

    # play media
    pygame.mixer.init()
    pygame.mixer.music.load(media_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

    # delete media
    os.remove(media_path)


####################################################### util

def get_random_string():
    return ''.join(random.choice(string.ascii_letters) for i in range(20))

def generate_media_name():
    random_str = get_random_string()
    return random_str + '.mp3'

def download_media(url):
    doc = requests.get(url, allow_redirects=True)
    media_name = generate_media_name()
    path = media_name 
    open(media_name, 'wb').write(doc.content)
    return path

