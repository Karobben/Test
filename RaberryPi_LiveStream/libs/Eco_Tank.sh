#!/usr/bin/env bash

while [ 1 -eq 1 ]
do
Name=$(date "+%Y_%m_%d_%H_%M_%S")
raspistill -o Pictures/$Name.jpg -w 2560 -h 1440 -v -vf

bash Blive &
sleep 3590

kill $(ps -u pi| grep ffmpeg| awk '{print $1}')
sleep 6
done
