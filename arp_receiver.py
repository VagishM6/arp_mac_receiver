import subprocess
import scapy.all as scapy
import re


# ip_range = int(input("[+] Enter range of IP to scan: "))
#
#
# def arp_ping(ip):
#     if ip > 24:
#         print("[-] Range exceeded the ip limit")
#     else:
#         store_ip = scapy.arping(f"192.168.1.1/{ip}")
#         return store_ip


# arp_res = arp_ping(ip_range)
# print("results: " + str(arp_res))





# # arp packet generator
# def scan(ip, mac):
#     # scapy.arping(ip)
#
#     # creating an instance of - scapy ARP class
#     arp_request = scapy.ARP(pdst=ip)
#     # list options of scapy ARP class parameters
#     # scapy.ls(arp_request)
#     print(arp_request.summary())
#
#     # creating an instance of - scapy Ether class
#     broadcast = scapy.Ether(dst=mac)
#     # list options of scapy Ether class parameters
#     # scapy.ls(broadcast)
#     print(broadcast.summary())
#
#
# # sending arp packets to the target ip
# scan("192.168.8.1/24", "ff:ff:ff:ff:ff:ff")


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