#!/bin/sh

echo 'Type the filename: '
read filename
suffix="_edited.txt"
edited="$filename$suffix"
# filename="18032011_edited.txt"
sudo youtube-dl -i -l -f 5 -a "$edited"
