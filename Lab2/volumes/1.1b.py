#!/usr/bin/env python3
from scapy.all import *
def print_pkt(pkt):
    pkt.show()

# icmp only
# pkt = sniff(iface='br-787664767f86', filter='icmp', prn=print_pkt)

# tcp
pkt = sniff(iface='br-787664767f86', filter='tcp and src host 10.9.0.1', prn=print_pkt)