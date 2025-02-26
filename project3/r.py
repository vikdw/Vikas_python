

class Reader():
    def __init__(self, txt_file):      
        with open(txt_file, 'r') as f:
            data= f.readlines()
            d = {}
            for x in data:
                x = x.rstrip().split(',') 
                d[x[0]]= [x[1],x[2]]
        self.data = d
        
        

    # def run(self):
    #     for k,v in self.data.items():
    #         if k == 'function':
    #             continue
    #         elif k =='add':
    #             print(f"result of {k} is: {self.add(int(v[0]),int(v[1]))}")
    #         elif k =='sub':
    #             print(f"result of {k} is: {self.sub(int(v[0]),int(v[1]))}")
    #         else:
    #             print(f"{k} key function not implemanted")