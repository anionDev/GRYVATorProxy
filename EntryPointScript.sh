#!/bin/bash

echo "--------------------"
echo "Tor-version:"
tor --version

if [ -z "$(ls -A ./userhome/etc_tor)" ]; then
   cp -r /etc/tor ./userhome/etc_tor
fi

if [ ! -f ./userhome/etc_tor/tor/torrc ]; then
    echo "torrc-file not found."
    exit 1
else
    echo "--------------------"
    echo "Tor-Configuration:"
    cat ./userhome/etc_tor/tor/torrc
    echo "--------------------"
    tor -f ./userhome/etc_tor/tor/torrc
fi
