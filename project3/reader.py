


# l =[]
# d = {}
# with open('data.txt', 'r') as f:
#     data= f.readlines()
#     for x in data:
#         x = x.rstrip().split(',') 
#         d[x[0]]= [x[1],x[2]]
#     print(d)

class Property:
    def add(self,a,b):
        print("adder called")
        return a+b
    def sub(self, a,b):
        print("Sub called")
        return a-b


class Reader(Property):
    def __init__(self, txt_file):
        
        with open(txt_file, 'r') as f:
            data= f.readlines()
            d = {}
            for x in data:
                x = x.rstrip().split(',') 
                d[x[0]]= [x[1],x[2]]
        self.data = d
        

    def run(self):
        for k,v in self.data.items():
            if k == 'function':
                continue
            # x = self.add(int(v[0]),int(v[1]))
            # print(x)
            elif k =='add':
                print(f"result of {k} is: {self.add(int(v[0]),int(v[1]))}")
            elif k =='sub':
                print(f"result of {k} is: {self.sub(int(v[0]),int(v[1]))}")
            else:
                print({f"{k} key function not implemanted"})
 

r = Reader('data.txt')
# print(r.data)
print(r.run())
# print(r.__dict__)

