#!/bin/bash
#----------------
# nmap-pr.sh
# Last Modified: 4/17/20
# Coder: Stefan Esquivel
# Oddities: It can be CPU intensive, be careful modifying the Nmap command as a
#			general scan causes printers to print uncontrollably.
#----------------

# grabs all number arguments in a list
args=("$@")
# clears the past entries in the list
true > active-ips.txt

# checks if there were any arguments
if [ -z "${args[*]}" ]; then
	# if none, it proceeds to hit every server
	for ((counter=1; counter<28; counter++))
	do
		# ignores branch 9, for now, may need to uncomment when branch 9 becomes active
		if [[ $counter -ne 9 ]]; then
			# retrieves IP via Nmap
			# output=$(nmap -p 21 X."$counter".Y.0/25)
			# apennds only the IPs to active-ips.txt
			echo "$output" | grep -o -E '([0-9]{1,3}\.){3}[0-9]{1,3}' >> active-ips.txt
		fi
	done

	# retrieves IPs from Head Office
	# output=$(nmap -p 21 X.99.Y.0/25)
	echo "$output" | grep -o -E '([0-9]{1,3}\.){3}[0-9]{1,3}' >> active-ips.txt
else
	# if the were arguments, it would proceed to record the IPs for the branches specified
	for e in "${args[@]}" 
	do
		# retrieves IP via Nmap
		# output=$(nmap -p 21 X."$e".Y.0/25)
		# outputs only the IPs to active-ips.txt
		echo "$output" | grep -o -E '([0-9]{1,3}\.){3}[0-9]{1,3}' >> active-ips.txt
	done
fi