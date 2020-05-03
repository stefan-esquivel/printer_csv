#!/bin/bash
# ----------------
# nmap-pr.sh
# Last Modified: 2/10/20
# Coder: Stefan Esquivel
# Oddities: None
# ----------------
# Reads IP from stdin
IP=$1
# Retrives the serial number
snmpwalk -v1 -Ov -c public "$IP" mib-2.43.5.1.1.17.1