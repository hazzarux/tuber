#!/bin/sh

for i in *.flv; do ffmpeg -i "$i" "`basename "$i" .flv`.mp3"; done
