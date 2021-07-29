#!/bin/bash

if [ -z "$(ls -A /userhome/etc_tor)" ]; then
   cp -r /etc/tor /userhome/etc_tor
fi

tor /userhome/etc_tor
