#!/bin/sh
CAPS_LOCK=$(xset q | grep -Po 'Caps Lock: *(off|on)' | grep -Po 'off|on')

notify-send --expire-time=1000 "Caps Lock: $CAPS_LOCK"
