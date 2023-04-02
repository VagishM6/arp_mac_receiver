# arp_mac_receiver
A python script that's able to receive mac addresses of connected devices.

The script will send a broadcasing signal to all the possible devices that it can find, asking for a range of ip addresses based on the subnet mask provided, within a network. In that way the script will be able to receive all the mac addresses of the device that are connected to the network through the ARP protocol.

## used modules
- scapy (pip install scapy)
- subprocess
- re
