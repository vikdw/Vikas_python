from scapy.all import *

data = rdpcap("./scapy/ecpri/ecpri.pcap")

d_l= [x for x in data]

d1 = d_l[1][Raw].load.hex()


data= []
for x in d1:
    # print(x, format(int(x, 16), '04b'))
    data.append(format(int(x, 16), '04b'))
# print(d1)
# print(data)


# data= ['0001', '0000', '0000', '0001', '0000', '0000', '0001', '0100', '0001', '0010', '0011', '0100', '1000', '0111', '0110', '0101', '0000', '1111', '0000', '1110', '0000', '1101', '0000', '1100', '0000', '1011', '0000', '1010', '0000', '1001', '0000', '1000', '0000', '0111', '0000', '0110', '0000', '0101', '0000', '0100', '0000', '0011', '0000', '0010', '0000', '0001', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0010', '0010', '0011', '0011', '0100', '0100', '0101', '0101']

mess_type={0:"User Plane", 1:"bit sequence", 2:"C plane", 3:"generic data", 4:"Remote mem access", 5:"delay measurement", 6:"emote Reset", 7:"Event Indication"}

def pkt_process(data):
    version= int(data[0], 2)
    concatination= int(data[1][-1],2)
    message_type= int(data[2]+data[3], 2)
    payload_size= int(data[4]+data[5]+data[6]+data[7], 2)
    eAxc_Id= data[8]+data[9]+data[10]+data[11]
    DU_Port_Id= int(eAxc_Id[:2], 2)
    BandSectorId=int(eAxc_Id[2:8], 2)
    CC_Id=int(eAxc_Id[8:12], 2)
    RU_PortId=int(eAxc_Id[12:], 2)

    seq_Id= int(data[12]+data[13], 2)
    eBit= int(data[14][0],2)
    sub_SeqId= int(data[14][1:]+data[15], 2)


    print(f"ECPRI version is: {version}")
    if concatination == 0:
        print(f"concatination bit is: {concatination}, its is last packet.")
    else:
        print(f"concatination bit is: {concatination}, its is not the last packet.")

    try:
        if message_type in mess_type:
            print(f"message type bit is {message_type}, its a {mess_type[message_type]}")
    except:
        print("not defined packet type.")
    print(f"Payload size is {payload_size} byte(s)")
    print(f"eAxC id : {DU_Port_Id} {BandSectorId} {CC_Id} {RU_PortId}")
    print(f"seq ID is: {seq_Id}")
    print(f"E Bit: {eBit}")
    print(f"sub seq iD: {sub_SeqId}")


for pkt in d_l:
    d1= pkt[Raw].load.hex()
    Bin_data=[]
    for x in d1:
        Bin_data.append(format(int(x, 16), '04b'))
    pkt_process(Bin_data)