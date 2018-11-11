#!/bin/sh
light -U 25

notify-send --expire-time=1000 "Brightness: $(light -G)%"
