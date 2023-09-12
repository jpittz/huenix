# Philips Hue Setup from phue
# This file only needs to be run once to initially connect to your bridge

# Imports phue Bridge library
from phue import Bridge

def hueSetup():
    global b
    b = Bridge('')  # b = Bridge('ip_of_your_bridge')

    # If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
    b.connect()

    return None
    
hueSetup()
