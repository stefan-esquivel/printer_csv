#!/usr/bin/python3
# ----------------
# Printer.py
# Last Modified: 4/17/20
# Coder: Stefan Esquivel
# Oddities: None
# ----------------


# printer object holds the info of the printer
class Printer:
    # init function sets up objects with characteristics
    def __init__(self, ip=None, label=None, mac=None, model=None, name=None, serial=None, time_stamp=None):
        # since ASL uses unique branch IPs, the second 8-bit number specifies the branch number
        self.branch = ip.split(".")[1]
        self.ip = ip
        self.label = label
        self.mac = mac
        self.model = model
        self.name = name
        self.serial = serial
        self.time_stamp = time_stamp

    # below are the accessors and modifiers of each object variable
    def get_branch(self):
        return self.branch

    def get_ip(self):
        return self.ip

    def set_ip(self, ip):
        self.ip = ip

    def get_label(self):
        return self.label

    def set_label(self, label):
        self.label = label

    def get_mac(self):
        return self.mac

    def set_mac(self, mac):
        self.mac = mac

    def get_model(self):
        return self.model

    def set_model(self, model):
        self.model = model

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_serial(self):
        return self.serial

    def set_serial(self, serial):
        self.serial = serial
    # To string function of the Printer object allows direct print of the printer object for printing purposes
    def __str__(self):
        x = [self.branch, self.ip, self.label, self.mac, self.model, self.name, self.nmap_banner, self.serial]
        return str(x)
