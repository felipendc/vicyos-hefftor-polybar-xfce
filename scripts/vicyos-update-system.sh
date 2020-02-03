#!/bin/bash

##########################################
### Script made by Felipe Ndc (Vicyos) ###
##########################################

# This command will open a new urxvt terminal window and run: "sudo pacman -Syu".
# If your Linux Distribution has a different terminal,
# replace "urxvt" with the name of your terminal.

# If you are running a Linux Distribution based on Ubuntu or Debian, 
# you will need to change: "sudo pacman -Syu" to "sudo apt-get update && sudo apt-get upgrade".

urxvt -e sh -c "yay -Syu --noconfirm"
