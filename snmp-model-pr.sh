#!/bin/bash
# ----------------
# nmap-pr.sh
# Last Modified: 2/10/20
# Coder: Stefan Esquivel
# Oddities: None
# ----------------
# Reads IP from stdin
IP=$1
# Retrieves the printer model name
snmpwalk -v1 -Ov -c public "$IP" SNMPv2-MIB::sysName.0 | cut -d' ' -f2-