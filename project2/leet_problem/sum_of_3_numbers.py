ar= [-1,0,1,2,-4,-1]

s= 1
th= 2
ls= len(ar)
l=[]
for x in range(0,ls-2):
        for y in range(s,ls-1):
            for z in range(th, ls):
                if (ar[x]+ ar[y]+ ar[z])==0:
                    t = [int(ar[x]), int(ar[y]), int(ar[z])]
                    t.sort()
                    if t not in l: 
                        l.append(list(t))
            th = th+1
        s = s+1
        th= s+1
print(l)

for x in l:
     print(sum(x))
    
          
     
     

            

# # print(l)
# # l = [x for x in l is sum(x)==3]
# print(l)

        



