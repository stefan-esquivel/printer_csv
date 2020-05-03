#!/bin/bash
#
#--------------
# Last Modified:
# Coder: Stefan & Triston
# Oddities: May require | between SSHPass and SCP on Linux
# ---------------

#password=""

for (( counter=1; counter<29; counter++))
	do
	if [ $counter -lt 10 ];
		then
			sshpass -p "$password" scp -o StrictHostKeyChecking=no id_rsa.pub sysadm@xserver0${counter}.sheret.com:/home/sysadm/.ssh/authorized_keys
	else
			sshpass -p "$password" scp -o StrictHostKeyChecking=no id_rsa.pub sysadm@xserver${counter}.sheret.com:/home/sysadm/.ssh/authorized_keys
	fi
	sshpass -p "$password" scp -o StrictHostKeyChecking=no id_rsa.pub sysadm@xserver99.sheret.com:/home/sysadm/.ssh/authorized_keys
done

