#!/bin/sh

notify-send --expire-time=1000 "Brightness: $(~/.config/i3/brightness.py -i)"
