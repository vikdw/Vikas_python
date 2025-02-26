import numpy as np

file= 'redis/input.csv'
d = {'test3':'this is test3', 'test4':'this is test4'}
# l = []
# m = []
# d1={}
# input_data=np.loadtxt(file,delimiter=',',dtype=str)

# with open(file, 'r') as read_f:
#     r = read_f.readlines()
#     print(r)
#     with open(file, 'w') as write_f:
#         for x in r:
#             print(x)
#             print(x.strip('\n').split())
#             for k in d.keys():
#                 print(k)
#                 if str(k) not in x.strip('\n').split():
#                     l.append(x)
#                     print(f"k is {k},  l is {l}")
#             if len(l)>1:
#                 write_f.write(l[0])
#                 m.append(l[0])
#                 l.clear()
#             else:
#                 l.clear()




def del_data(d: dict,file=file):

    print(file)
    l=[]
    # file = self.file if file=={} else file
    with open(file, 'r') as read_f:
        r = read_f.readlines()
        print(r)
        with open(file, 'w') as write_f:
            for x in r:
                print(f"x is {x}")
                if len(d.keys())==1:
                    if str(k.keys()[0]) not in x.strip('\n').split():
                        write_f.write(x)
                if len(d.keys())>1:
                    for k in d.keys():
                        if str(k) not in x.strip('\n').split():
                            l.append(x)
                            print(f"l is {l}")
                    if len(l)>1:
                        write_f.write(l[0])
                        l.clear()
                    else:
                        l.clear()
print(file)
del_data(d,file)
          


   
        


