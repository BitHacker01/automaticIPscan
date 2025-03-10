#!/bin/bash

for ip in {1..254};
do
	echo "$ip"
	ping -c 1 $1.$ip | grep 64 | cut -d " " -f 4 | tr -d ":"
done

# usage: ./activeIPscan.sh 192.168.10

