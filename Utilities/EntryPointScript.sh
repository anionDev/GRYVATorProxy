#!/bin/bash

if [ -z "$(ls -A /userhome/etc_tor)" ]; then
   cp -r /etc/tor ./etc_tor
fi

if [ ! -f ./etc_tor/tor/torrc ]; then
    echo "torrc-file not found."
else
   echo "--------------------"
   echo "Tor-Configuration:"
   cat ./etc_tor/tor/torrc
   echo "--------------------"

   tor -f ./etc_tor/tor/torrc
fi
