#!/bin/bash

chown -R root:0 /var_lib/tor
tor -f /etc_tor/torrc
