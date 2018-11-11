#!/bin/sh
pactl set-sink-mute 0 toggle

SINK=$( pactl list short sinks | sed -e 's,^\([0-9][0-9]*\)[^0-9].*,\1,' | head -n 1 )
MUTE=$( pactl list sinks | grep '^[[:space:]]Mute:' | head -n $(( $SINK + 1 )) | tail -n 1 | grep -Po 'yes|no' )

notify-send --expire-time=1000 "Mute: $MUTE"
