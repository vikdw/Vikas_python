import pyshark
from copy import deepcopy
import numpy as np
import pandas as pd


cap = pyshark.FileCapture('./scapy/2ue_attach1.pcap')

l = [x for x in cap if 'F1AP' in x]
message_code= {11:'RRC_Initial_message', 12:'RRC_setup_message', 13:'RRC+NAS_message', 6:'Release'}
# print(l[0])
# print(f"{x.F1AP.procedureCode}")
# print(x.F1AP.field_names)
# print(x.F1AP.c_rnti)
# print(x.F1AP.gnb_du_ue_f1ap_id)
# print(x.F1AP.gnb_cu_ue_f1ap_id)
d_du={}
d_cu={}
for p in l:
        if p.F1AP.procedureCode == '11' :
            d_du[p.F1AP.gnb_du_ue_f1ap_id]= p.F1AP.c_rnti
        if p.F1AP.procedureCode == '12' :  
            d_cu[p.F1AP.gnb_du_ue_f1ap_id]= p.F1AP.gnb_cu_ue_f1ap_id
# print(d_du, d_cu)
for k in d_du:
     d_du[k]=[d_du[k]]
# print(d_du, d_cu)
for k,v in d_du.items():
     d_du[k].append(d_cu[k])
# print(d_du, d_cu)
d={}
m=[]
n=[]
q=[]
for k,v in d_du.items():
    for p in l:         
        if int(p.F1AP.gnb_du_ue_f1ap_id) == int(k):
            time = p.frame_info.time_epoch
            code = p.F1AP.procedureCode
            source=p.IP.src_host
            destination=p.IP.dst_host
            cu_ue_id= d_cu[k]
            du_ue_id= k
            crnti=v[0]
            m = [crnti,time,source, destination, code, cu_ue_id, du_ue_id]
            n.append(m) 
    q = deepcopy(n)
    # print(f"value of q after deep copy: {q}")                   
    d[v[0]]= q
    n.clear()
    

# print(d)

data = [(key, np.array(value)) for key, value in d.items()]
# dtype = [('key', 'U10'), ('values', 'O')]
# npArray= np.array(data, dtype=dtype)
df = pd.DataFrame(data, columns=["C-RNTI", "data"])
# df = pd.DataFrame(data)

print(df['data'])
with pd.ExcelWriter("t_output.xlsx", engine="openpyxl") as writer:

    total_data=pd.DataFrame(columns=['CRNTI','time','source', 'destination', 'code', 'cu_ue_id', 'du_ue_id'])
    for key, row in df.iterrows():
        sheet_name= row['C-RNTI']
        ue_data=pd.DataFrame(row['data'],columns=['CRNTI','time','source', 'destination', 'code', 'cu_ue_id', 'du_ue_id'] )
        total_data=pd.concat([total_data, ue_data[1:]], ignore_index=True)
        # print(total_data)
        # print(sheet_name)
        # print(ue_data)
        ue_data.to_excel(writer, sheet_name=sheet_name, index=False, header=False)
    total_data.to_excel(writer, sheet_name="ALL_UE", index=False, header=False)        

            
    
