# huenix

## Purpose

I've never written shell before, so this project's purpose is to learn it. That aside, the function of this repo is to use shortcuts in terminal to make quick changes to my hue lights such as turning them on and off quickly or setting pre-defined scenes.

## Setup

For huenix to work you'll need to connect your [Philips Hue](https://www.philips-hue.com/) Bridge to Python using `hue-setup.py`. This only needs to be done once. You'll need you Bridge IP address, which can be found within the Philips Hue App. 

You'll also need to open `lights.py` and enter your bridge IP, as well as (for now) specify the lights you'd like huenix to control using either their name or number.

This process requires the [phue](https://github.com/studioimaginaire/phue) library which can be installed using either:

```
sudo easy_install phue
```
or
```
pip install phue
```

## Current Usage (Unfinished, currently **not** functional)

Run `./huenix.sh` in terminal. Current limitation is that you must be in the `/huenix` directory. You'll then be asked to enter an ON or OFF value and then brightness as a percentage. These arguements are then passed into `lights.py` for the main program.
