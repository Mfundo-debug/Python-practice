"""
Implement a function to scan the network and identify devices connected to it.
"""
from scapy.all import ARP, Ether, srp

def scan_network(ip):
    """
    Scan the network and identify devices connected to it.
    """
    arp = ARP(pdst=ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp
    result = srp(packet, timeout=3, verbose=0)[0]
    clients = []
    for sent, received in result:
        clients.append({'ip': received.psrc, 'mac': received.hwsrc})
    return clients

devices = scan_network("192.168.1.1/24")
print("Available devices in the network:")
print("IP" + " "*18+"MAC")
for client in devices:
    print("{:16}    {}".format(client['ip'], client['mac']))