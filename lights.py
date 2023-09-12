import sys # allows terminal args
from phue import Bridge # for Philips Hue

def hueSetup():
    global b
    b = Bridge('')  # b = Bridge('ip_of_your_bridge')

    global lights
    lights = [11, 12]  # Use lights you want

    return None

def main(arg1, arg2):
    # takes arguments from shell
    lightStatus = arg1 # standardises input
    lightBrightness = int(arg2)

    if lightStatus == "ON":
        lightStatus = "Lights On"
        
    elif lightStatus == "OFF":
        lightStatus = "Lights Off"
        lightBrightness = int(0) # defaults brightness to 0 if lights are off
    else:
        lightStatus = "Invalid" # temp error handling

    print(lightStatus)
    print(lightBrightness, "% Brightness")

hueSetup()
main((sys.argv[1]).upper(), sys.argv[2])









