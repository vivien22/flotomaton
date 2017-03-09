#!/bin/bash

# For SDL
sudo apt-get update
sudo apt-get upgrade

sudo apt-get install libsdl1.2-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libportmidi-dev

# Then install pygame
sudo apt-get build-dep python-pygame
sudo apt-get install mercurial
sudo apt-get install libfreetype6-dev
sudo pip install hg+http://bitbucket.org/pygame/pygame

