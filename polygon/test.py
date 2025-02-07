# import json


# def read_json(json_file):
#     with open(json_file, 'r') as file:
#         data = json.load(file)    
#     SideRadius=[]
#     TC = []
#     passing_criteria= []   
#     for i in data:
#         temp =(data[i]['side'],data[i]['radius'])
#         SideRadius.append(temp)
#         del temp
#         TC.append(data[i]['TC'])
#         passing_criteria.append(data[i]['Pass'])

#     return SideRadius, TC, passing_criteria 

# SideRadius, TC, passing_criteria = read_json('/home/vikasdw/python/polygon/input.json')

# print(SideRadius, TC, passing_criteria)



import socket

print(socket.gethostname())
