#!/bin/bash
# ----------------
# arp-lable-pr.sh
# Last Modified: 4/17/20
# Coder: Stefan Esquivel
# Oddities: Requierse the user to input the Xserver password... ran out of time to use ssh pass :(
#           to iterate you may need to gen a ssh kay asnd store it on the Xserver
# ----------------

# Takes an ip address string from the stdin
IP=$1
# Checks if it is a head office IP
if [[ $IP == 10.99* ]] ;
	then
# Builds the ip for Xserver99
	SUB_IP=$(echo "$IP" | grep -o -E '([0-9]{1,3}\.){2}')255.94
else
# Builds the ip for branch Xserver
	SUB_IP=$(echo "$IP" | grep -o -E '([0-9]{1,3}\.){2}')255.2
fi
# ssh into the server and dose an arp ping combo to retrieve the lable of the printer
ssh -c aes128-cbc sysadm@"$SUB_IP" "ping $IP -c 1 >/dev/null; arp $IP" | grep -o -E '([[:xdigit:]]{1,2}:){5}[[:xdigit:]]{1,2}'