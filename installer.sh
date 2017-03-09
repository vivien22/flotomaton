#!/bin/bash

# update
sudo rpi-update
sudo apt-get update
sudo apt-get dist-upgrade

# Execute all installer.sh files included un tools directory
for file in tools/*-installer.sh; do ./$file; done

