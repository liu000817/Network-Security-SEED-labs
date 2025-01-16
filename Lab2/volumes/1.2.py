#!/usr/bin/env python3
from scapy.all import *

ip = IP(src = '8.8.8.8', dst = '10.9.0.5')
icmp = ICMP()
packet = ip/icmp
packet.show()
send(packet) 