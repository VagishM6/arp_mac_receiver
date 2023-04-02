import subprocess
import scapy.all as scapy
import re

get_ip = input("[+] IP > ")
get_mac = "ff:ff:ff:ff:ff:ff"


def scan(ip, mac):
    # creating
    arp_request = scapy.ARP(pdst=ip)
    print(arp_request)
    arp_request.show()

    # broadcast MAC address
    broadcast = scapy.Ether(dst=mac)
    print(broadcast)
    broadcast.show()

    arp_request_broadcast = broadcast/ arp_request
    print(arp_request_broadcast)
    arp_request_broadcast.show()


scan(get_ip, get_mac)