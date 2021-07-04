#!/bin/bash

counter=0
while test $counter -lt 3; do
        counter=$((counter+1))
        echo "counter: $counter"
        cat /etc_tor/torrc | grep HiddenService
        sleep 3
done
echo start

chown -R root:0 /var_lib/tor
tor -f /etc_tor/torrc
