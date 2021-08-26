import subprocess
import optparse
import re

def get_args():
	prs = optparse.OptionParser()
	prs.add_option("-i","--interface",dest="interface",help="Inteface to change mac")
	prs.add_option("-m","--mac",dest="mac",help="New mac address")
	(opt,arg) = prs.parse_args()

	if not opt.interface:
		prs.error("[-] You forgot to specify interface")
	elif not opt.mac:
		prs.error("[-] You forgot to specify mac")
	return opt

def change_mac(interface,newMac):
	subprocess.call(["ifconfig",interface,"down"])
	subprocess.call(["ifconfig",interface,"hw","ether",newMac])
	subprocess.call(["ifconfig",interface,"up"])

def get_current_mac(interface):
	interface_data = subprocess.check_output(["ifconfig",interface])
	interface_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",interface_data)

	if not interface_mac:
		print("[-] Could not read mac address")
	else:
		return interface_mac.group(0)

def compare_mac(inputMac,currentMac):
	if inputMac == str(currentMac):
		print("[+] Mac address successfully changed")
	else:
		print("[-] Error changing mac address")

opt = get_args()

interface = opt.interface
newMac = opt.mac

change_mac(interface,newMac)
currentMac = get_current_mac(interface)
compare_mac(newMac,currentMac)