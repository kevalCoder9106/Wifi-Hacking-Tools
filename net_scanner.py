import scapy.all as scapy
import argparse

def get_argument():
	prs = argparse.ArgumentParser()
	prs.add_argument("-t","--target",dest="target",help="IP Address of target")
	options = prs.parse_args()
	return options	

def scan(ip):
	arp_req = scapy.ARP(pdst=ip)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	packet = broadcast/arp_req
	ans = scapy.srp(packet, timeout=1,verbose=False)[0]
	
	
	
	client_list = []
	for element in ans:
		client_data = {"ip":element[1].psrc,"mac":element[1].hwsrc}
		client_list.append(client_data)

	return client_list

def print_scan_data(client_list):
	print("IP\t\t\tMac Address\n--------------------------------------------")
	for element in client_list:
		print(element["ip"] + "\t\t" + element["mac"])

opt = get_argument()
client_list = scan(opt.target)
print_scan_data(client_list)
