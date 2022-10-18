#!/bin/bash

echo "--------------------"
echo "Tor-version:"
tor --version

if [ -z "$(ls -A ./userhome/etc_tor)" ]; then
    echo "Initialize for first usage..."
   cp -r /etc/tor ./userhome/etc_tor
fi

echo "--------------------"
if [ ! -f ./userhome/etc_tor/tor/torrc ]; then
    echo "torrc-file not found."
    echo "--------------------"
    exit 1
else
    echo "Tor-Configuration:"
    cat ./userhome/etc_tor/tor/torrc
    echo "--------------------"
    echo "Start tor"
    tor -f ./userhome/etc_tor/tor/torrc
fi
