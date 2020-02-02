#!/usr/bin/env sh

# More info : https://github.com/jaagr/polybar/wiki

# Install the following applications for polybar and icons in polybar if you are on ArcoLinuxD
# awesome-terminal-fonts
# Tip : There are other interesting fonts that provide icons like nerd-fonts-complete

# Terminate already running bar instances
killall -q polybar


# Wait until the processes have been shut down

while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done

# Launch mainbar
polybar --reload vicyos-mainbar -c ~/.config/polybar/config &
         
