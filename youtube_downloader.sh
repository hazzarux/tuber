#!/bin/sh

echo 'Type the filename: '
read filename
$edited="${filename}_edited.txt"
#filename="18032011_edited.txt"
sudo youtube-dl -i -l -f 5 -a "$edited"
