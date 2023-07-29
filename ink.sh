#!/bin/sh

while true
do
	log=$(tail -n 1 direwolf-logs/2023-07-29.log)
	papirus-write "$log" --fsize 15
	sleep 30
done
