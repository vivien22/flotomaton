#!/bin/bash
while true
do
    if (pgrep launcher) ; then 
        sleep 1
    else
        ./launcher.sh &
    fi
done
