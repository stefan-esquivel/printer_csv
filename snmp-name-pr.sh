#!/bin/bash
# ----------------
# nmap-pr.sh
# Last Modified: 2/10/20
# Coder: Stefan Esquivel
# Oddities: CPU intensive, causes printer glitches
# ----------------
# Reads IP from stdin
IP=$1
# Retrives the printer brand name
snmpwalk -Ov -c public "$IP" SNMPv2-MIB::sysDescr.0 | cut -d' ' -f2