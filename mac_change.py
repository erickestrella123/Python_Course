from ssl import Options
import subprocess
import optparse
import re

from click import option

def get_arguments():
    parser = optparse.OptionParser()

    parser.add_option("-i", "--interface", dest = "interface", help="Interface para cambiar la Dirrecion MAC")
    parser.add_option("-m", "--mac", dest = "new_mac", help="Nueva Dirrecion MAC")

    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Por favor indicar una Interfaz, usa --help para mas informacion")
    elif not options.new_mac:
        parser.error("[-] Por favor indicar una Dirrecion MAC, usa --help para mas informacion")
    return options

def change_mac(interface, new_mac):
    print (" ")
    print ("[+] Cambiando Dirreccion MAC para " + interface + " a " + new_mac)
    print (" ")
    print("[+] La MAC se cambio correctamente a " + new_mac)
    print (" ")

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

options = get_arguments()

change_mac(options.interface,options.new_mac)
