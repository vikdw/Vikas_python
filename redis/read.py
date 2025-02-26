import numpy as np

file= 'redis/input.csv'
d = {'test3':'this is test3', 'test4':'this is test4'}

class read_data():
    def __init__(self, file):
        self.file= file
        
    def read_file(self,file=file):
        file = self.file if file=={} else file
        self.input_data=np.loadtxt(file,delimiter=',',dtype=str)
        return self.input_data 
    
    def add_data(self, d: dict, file=file):
        file = self.file if file=={} else file
        with open(file, 'a') as f:
            for k, v in d.items():
                l = f"{k}, {v}"
                f.write('\n')
                f.write(l)

    def del_data(self,  d: dict,file=file):
        l=[]
        file = self.file if file=={} else file
        with open(file, 'r') as read_f:
            r = read_f.readlines()
            with open(file, 'w') as write_f:
                for x in r:
                    if len(d.keys())==1:
                        if str(k.keys()[0]) not in x.strip('\n').split():
                            write_f.write(x)
                    if len(d.keys())>1:
                        for k in d.keys():
                            if str(k) not in x.strip('\n').split():
                                l.append(x)
                        if len(l)>1:
                            write_f.write(l[0])
                            l.clear()
                        else:
                            l.clear()


        



# r = read_data(file)
# print(r.read_file())
# r.add_data(d,file)
# print(r.read_file())
# r.del_data(d)
# print(r.read_file())


