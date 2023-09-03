import sys

# takes arguments from shell
lightStatus = (sys.argv[1]).upper() # standardises input
lightBrightness = int(sys.argv[2])

if lightStatus == "ON":
    lightStatus = "Lights On"
elif lightStatus == "OFF":
    lightStatus = "Lights Off"
    lightBrightness = int(0) # defaults brightness to 0 if lights are off
else:
    lightStatus = "Invalid" # temp error handling

print(lightStatus)
print(lightBrightness, "% Brightness")









