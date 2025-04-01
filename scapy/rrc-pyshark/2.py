from scapy.all import rdpcap

packets = rdpcap("./scapy/2ue_attach1.pcap")

for pkt in packets:
    print(pkt.show())