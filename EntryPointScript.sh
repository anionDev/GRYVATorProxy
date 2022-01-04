#!/bin/bash

if [ -z "$(ls -A /Workspace/userhome/etc_tor)" ]; then
   cp -r /etc/tor ./etc_tor
fi

if [ ! -f ./etc_tor/tor/torrc ]; then
    echo "torrc-file not found."
    exit 1
else
    echo "--------------------"
    echo "Tor-Configuration:"
    cat ./etc_tor/tor/torrc
    echo "--------------------"
    tor --version
    echo "--------------------"
    tor -f ./etc_tor/tor/torrc
fi
