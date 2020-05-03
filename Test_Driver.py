#!/usr/bin/python3
# ----------------
# Test_Driver.py
# Last Modified: 4/17/20
# Coder: Stefan Esquivel
# Oddities: Works only on mac, you will need to also need to add you ssh key to all the Xservers
# ----------------

# import made printer script tools
import Printer_list_to_csv
# tool for arguments
import argparse


# Main function that controles the whole script
def main():
    # Add parcer for user options
    parser = argparse.ArgumentParser(
        description="Printer Identifier to retrieve valuable printer information and stores it to a csv file",
        epilog="If there are any questions, please contact the author at sesquivel@uvic.ca")
    # all instructions can be found by running ./Test_Driver -h and for csv commands run ./Test_Driver csv -h
    parser.add_argument("-r", "--ricoh", action="store_true", help="stores only RICOH printers to the csv. Warning Older RICOH printers will not be detected!")
    parser.add_argument("-p", "--print", action="store_true", help="prints Information to stdout")
    subparsers = parser.add_subparsers(help='tools for csv')
    parser_output = subparsers.add_parser('csv', help=("specifies the data on the csv; no specification"
                                                       " will show everything"))
    parser_output.add_argument("-br", "--branch", type=int, metavar='N', nargs='*',
                               help="includes printers at the branch number specified in the positon of N: no argument will produce a csv file consisting of all of them")
    parser_output.add_argument("-ip", "--ip_address", action="store_true", help=("includes the ip adress"))

    parser_output.add_argument("-la", "--label", action="store_true", help=("includes the printer label from"
                                                                            " cups"))
    parser_output.add_argument("-ma", "--mac_adress", action="store_true", help="includes the mac address")

    parser_output.add_argument("-mo", "--model", action="store_true", help="includes the model number")

    parser_output.add_argument("-na", "--name", action="store_true", help="includes the name")

    parser_output.add_argument("-se", "--serial", action="store_true", help="includes the searial number")

    # Parcess all the arguments and stores it into a arg arpument, printing will print a list of the arguments
    args = parser.parse_args()

    try:
        # if no csv options are used all of the information will output
        if(args.branch is None and args.ip_address is False and args.label is False and args.mac_adress is False and args.model is False and args.name is False and args.serial is False):
            args.branch = []
            args.ip_address = True
            args.label = True
            args.mac_adress = True
            args.model = True
            args.name = True
            args.serial = True

        # gabs information

        # populates active ip list if you clarify the branch this process is quicker
        Printer_list_to_csv.populate_printer_list(args.branch)
        # uses ping arp combo to printer info see Printer_list_to.csv.py for more information
        Printer_list_to_csv.get_printer_info_from_arp(args.mac_adress, args.label)
        # uses snmp info see Printer_list_to.csv.py for more information
        Printer_list_to_csv.get_printer_info_from_snmp(args.serial, args.name, args.model, args.ricoh)

        # print to stdout
        if args.print:
            Printer_list_to_csv.print_my_list(args.branch, args.ip_address, args.label, args.mac_adress, args.model, args.name, args.serial, args.ricoh)

        Printer_list_to_csv.output_to_csv(args.branch, args.ip_address, args.label, args.mac_adress, args.model,
                                          args.name, args.serial, args.ricoh)
    except AttributeError:
        print("No CSV arguments made! Printing to stdout!")
        # if not csv arguments are made all the information will output to stdout

        # populates active ip list if you clarify the branch this process is quicker
        Printer_list_to_csv.populate_printer_list([])
        # uses ping arp combo to printer info see Printer_list_to.csv.py for more information
        Printer_list_to_csv.get_printer_info_from_arp(True, True)
        # uses snmp info see Printer_list_to.csv.py for more information
        Printer_list_to_csv.get_printer_info_from_snmp(True, True, True, False)
        # Prints to stdout
        Printer_list_to_csv.print_my_list([], True, True, True, True, True, True, True)


if __name__ == '__main__':
    main()
