#!/bin/sh
i3status | while :
do
    read line
    CAPSLOCK=$(xset q | grep -Po 'Caps Lock:\s*(off|on)' | grep -Po 'off|on')
    echo "⇪: $CAPSLOCK | $line" || exit 1
done
