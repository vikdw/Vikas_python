import pyshark


cap = pyshark.FileCapture('./scapy/ecpri/ecpri_iq.pcap')
# cap = pyshark.FileCapture('./scapy/ecpri/ecpri.pcap')






def check_CU_Plane(pkt):
    print("checking if packet is C-plane or U-plane")
    # print(pkt['ECPRI'].eventtype)
    print(pkt['ECPRI'].type)
    if str(pkt['ECPRI'].type) =="0x00":
        print("U-Plane packet")
        UPlane_process(pkt)
    elif str(pkt['ECPRI'].type) =="0x01":
        pass
        # print("its bit sequence")
        # print(pkt)
    elif str(pkt['ECPRI'].type) =="0x02":
        CPlane_process(pkt)
        # print("C-Plane packet")
    else:
        pass
        # print("its other packets")
    # print(pkt['ECPRI'].field_names)


def UPlane_process(pkt):
    print("its uplane pkt")
    print(pkt['ECPRI'])
    print(pkt['ECPRI'].field_names)
    print(pkt['ORAN_FH_CUS'])
    print(f"eAxC id is:- {pkt['ORAN_FH_CUS'].c_eaxc_id}")
    print(f"data direction is:- {pkt['ORAN_FH_CUS'].data_direction}")
    print(pkt['ORAN_FH_CUS'].field_names)
    ecpri_payload = bytes.fromhex(pkt.ecpri.payload.replace(":", ""))
    print(ecpri_payload)
    num_prbs = 12
    offset = 0
    for prb in range(num_prbs):
        udCompHdr = int.from_bytes(ecpri_payload[offset:offset+4], byteorder="big")
        print(udCompHdr)
        compression_type = (udCompHdr >> 28) & 0x0F  # Bits 0-3
        bitwidth = (udCompHdr >> 24) & 0x0F  # Bits 4-7
        iq_data_size = udCompHdr & 0xFFFF  # Bits 16-31
        print(f"PRB {prb}:")
        print(f"  Compression Type: {compression_type}")
        print(f"  Bitwidth: {bitwidth} bits")
        print(f"  IQ Data Size: {iq_data_size} bytes")
        offset += 4 + iq_data_size 

def CPlane_process(pkt):
    print("its Cplane pkt")
    print(pkt['ECPRI'])
    print(pkt['ECPRI'].field_names)
    print(pkt['ORAN_FH_CUS'])
    print(f"eAxC id is:- {pkt['ORAN_FH_CUS'].c_eaxc_id}")
    print(f"data direction is:- {pkt['ORAN_FH_CUS'].data_direction}")
    print(pkt['ORAN_FH_CUS'].field_names)



for pkt in cap:
    check_CU_Plane(pkt)