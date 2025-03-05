# l = [3,4,7,2,-3,1,4,2]
l = [4,2,1,6,3,1,2]
s= 0
e = 0
t= l[0]
c = 0
# for x in l:
#     n = s[-1]+x
#     s.append(n)

# print(s)
while s<len(l):
    if s>e:
        e=s
        t= l[s]
    if t<12:
        e = e+1
        if e == len(l):
            break
        t =t +l[e]
    elif t>12:
        t = t-l[s]
        s = s+1
    else:
        print(f"count incrase {l[s]}")
        c =c+1
        t = t-l[s]
        s = s+1

print(c)






