#!/bin/bash
while true
do
    if (pgrep launcher) ; then 
        sleep 2
    else
        ./launcher.sh &
    fi
done
