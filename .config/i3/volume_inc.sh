#!/bin/bash
#!/bin/sh
pactl set-sink-volume 0 +5%

SINK=$( pactl list short sinks | sed -e 's,^\([0-9][0-9]*\)[^0-9].*,\1,' | head -n 1 )
VOLUME=$( pactl list sinks | grep '^[[:space:]]Volume:' | head -n $(( $SINK + 1 )) | tail -n 1 | sed -e 's,.* \([0-9][0-9]*\)%.*,\1,' )
VOLUME_INFO=$( pactl list sinks | grep '^[[:space:]]Volume:' | head -n $(( $SINK + 1 )) | tail -n 1 | awk '{$1=$1};1' )

notify-send --expire-time=1000 "Volume: $VOLUME%"
