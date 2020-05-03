#!/usr/bin/python3
# ----------------
# Printer-list-to-csv.py
# Last Modified: 4/17/20
# Coder: Stefan Esquivel
# Oddities: Need ssh keys on the server to prevet password from constantly being asked
#           and also needs to be run on a mac
# ----------------

# important libraries to run script
import subprocess
import re
import Printer as mp
import Printer_list as pl

# printer list object to store all the printer information
my_list = pl.Printer_list()

# ------------------
# NAME: get_printer_info_from_arp
#
# PURPOSE: Grabs the mac adress and label using helper bash scripts
#
# PRECONDITIONS: None
#
# PARAMETERS: Two Bools
# -------------------
def get_printer_info_from_arp(mac_bool, label_bool):
    print("Grabbing info from ping>arp...")
    # iterates through entire printer list
    for e in my_list:
        # if the user wants to view that mac address, it will be recorded
        if mac_bool is True:
            try:
                # the bash script executes
                mac = subprocess.check_output(["./arp-mac-pr.sh", e.get_ip()]).decode('ascii').strip('\n')
                # mac is set
                e.set_mac(mac)
            except subprocess.CalledProcessError:
                # error if the mac retrieval failed
                print("Can't retrive mac address from \"" + e.get_ip() + "\"!")
        # if the user wants to view that label, it will be recorded
        if label_bool is True:
            try:
                label = subprocess.check_output(["./arp-label-pr.sh",
                                                e.get_ip()]).decode('ascii').strip('\n')
                e.set_label(label)
            except subprocess.CalledProcessError:
                # error if the mac retrival failed
                print("Can't retrive label from \"" + e.get_ip() + "\"!")
    print("Done")

# ------------------
# NAME: get_printer_info_from_snmp
#
# PURPOSE: Retrives serial, name and model using bash tools
#
# PRECONDITIONS: None
#
# PARAMETERS: 3 bools
# -------------------
def get_printer_info_from_snmp(serial_bool, model_bool, name_bool, ricoh_bool):
    print("Grabbing info from snmp...")
    # regular expression patern to grab the label
    pattern = re.compile("(?<=\")(.*)(?=\")", re.IGNORECASE)
    for e in my_list:
        # if the user wants to view that mac address, it will be recorded
        if serial_bool is True:
            try:
                res = subprocess.check_output(["snmpwalk", "-v1", "-Ov", "-c", "public", e.get_ip(),
                                               "mib-2.43.5.1.1.17.1"]).decode('ascii')
                match = pattern.search(res)
                if match is not None:
                    serial = res[match.span()[0]:match.span()[1]]
                    e.set_serial(serial)
                else:
                    print("Can't retrive serial from \"" + e.get_ip() + "\"! Exists but cant find serial string!")
            except subprocess.CalledProcessError:
                print("Can't retrive serial from \"" + e.get_ip() + "\"! Dose not exist!")
        # if the user wants to view that mac address, it will be recorded
        if model_bool is True:
            try:
                model = subprocess.check_output(["./snmp-model-pr.sh", e.get_ip()]).decode('ascii').strip('\n')
                if model is not None:
                    e.set_model(model)
                else:
                    print("Can't retrive model from \"" + e.get_ip() + "\"! Exists but cant find model string!")
            except subprocess.CalledProcessError:
                print("Can't retrive model from \"" + e.get_ip() + "\"! Dose not exist!")

        # if the user wants to view that name, it will be recorded, the ricoh argument will record the name but will not output unless the name is requested
        if ricoh_bool is True or model_bool is True:
            try:
                name = subprocess.check_output(["./snmp-name-pr.sh", e.get_ip()]).decode('ascii').strip('\n')
                if name is not None:
                    e.set_name(name)
                else:
                    print("Can't retrive model from \"" + e.get_ip() + "\"! Exists but cant find name string!")
            except subprocess.CalledProcessError:
                print("Can't retrive name from \"" + e.get_ip() + "\"! Dose not exist!")
    print("Done")


# helper print to csv method
def output_to_csv(g_br, g_ip, g_lab, g_mc, g_mod, g_na, g_ser, g_ricoh):
    my_list.copy_to_csv(g_br, g_ip, g_lab, g_mc, g_mod, g_na, g_ser, g_ricoh)


# helper print to csv method
def print_my_list(g_br, g_ip, g_lab, g_mc, g_mod, g_na, g_ser, g_ricoh):
    my_list.print_list(g_br, g_ip, g_lab, g_mc, g_mod, g_na, g_ser, g_ricoh)


# Populates printer list using nmap
def populate_printer_list(branch_numbers):
    print("Updateing Printer List...")
    command = ["./nmap-pr.sh"]

    if branch_numbers:
        for i in range(0, len(branch_numbers)):
            command.append(str(branch_numbers[i]))

    subprocess.check_output(command)
    with open("active-ips.txt", mode="r") as ip_file:
        for line in ip_file:
            line = line.strip("\n")
            my_list.add_printer(mp.Printer(ip=line))
        ip_file.close()
    print("Done")
