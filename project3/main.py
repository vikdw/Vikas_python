
import p
import r



class Main:
    def __init__(self, file):
        self.d_dict= r.Reader(file)
        self.property= p.Property()

    def run(self):
        for k,v in self.d_dict.data.items():
            if k == 'function':
                continue
            else:
                a = getattr(self.property, k)
                print(a(int(v[0]),int(v[1])))
            #     # print(f"result of {k} is: {self.property.add(int(v[0]),int(v[1]))}")
            # elif k =='sub':
            #     print(f"result of {k} is: {self.property.sub(int(v[0]),int(v[1]))}")
            # else:
            #     print(f"{k} key function not implemanted")


m = Main('data.txt')
print(m.d_dict.data)
m.run()