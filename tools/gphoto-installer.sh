#!/bin/bash

# gphoto2 & libgphoto2
sudo apt-get install gphoto2 libjpeg9-dev
wget https://raw.githubusercontent.com/gonzalo/gphoto2-updater/master/gphoto2-updater.sh && chmod +x gphoto2-updater.sh && sudo ./gphoto2-updater.sh
rm gphoto2-updater.sh

# Python gphoto2
sudo apt-get install python-dev
sudo pip install gphoto2
