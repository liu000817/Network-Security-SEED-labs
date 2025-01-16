#!/usr/bin/env python3
from scapy.all import *
def print_pkt(pkt):
    pkt.show()

# icmp only
# pkt = sniff(iface='br-0905f650f9f2', filter='icmp', prn=print_pkt)

# tcp
# pkt = sniff(iface='br-0905f650f9f2', filter='tcp and src host 10.9.0.1', prn=print_pkt)

# subnet
pkt = sniff(iface='br-0905f650f9f2', filter='net 10.9.0.0/24', prn=print_pkt)