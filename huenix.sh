#!/bin/sh

echo """
########
 Huenix
########
"""

echo "Lights ON / OFF? "
read onState
echo "Light brightness %:"
read brightness
echo
/usr/bin/python3 lights.py $onState $brightness
echo
