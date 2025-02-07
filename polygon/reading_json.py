import json


def read_json(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)    
    SideRadius=[]
    TC = []
    PassingCriteria= []   
    for i in data:
        temp =(data[i]['side'],data[i]['radius'])
        SideRadius.append(temp)
        del temp
        TC.append(data[i]['TC'])
        PassingCriteria.append(data[i]['Pass'])

    return SideRadius, TC, PassingCriteria 


if __name__ == "__main__":
    SideRadius, TC, Passing_criteria = read_json("/home/vikasdw/python/polygon/input.json")
    print(SideRadius)
    print(TC)