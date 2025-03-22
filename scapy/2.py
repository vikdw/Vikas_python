import pyshark
# 
cap = pyshark.FileCapture('./scapy/2ue_attach1.pcap')

l = [x for x in cap if 'F1AP' in x]
x = l[11]
print(x.F1AP.field_names)
print(x.F1AP)
print(x.F1AP.f1ap_pdu, x.F1AP.rrccontainer)