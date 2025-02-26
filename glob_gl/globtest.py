d = {'a':1,'c':3,'b':2}
# sort_dk={x:d[x] for x in sorted(d, key=lambda d:d)}
# sort_dv={x:d[x] for x in sorted(d, key=lambda d:d.values())}
# print(sort_dk)
# print(sort_dv)
l =list(d.values())
print(l)
l.sort()
print(l)
t={}
for i in l:
    for k,v in d.items():
        if i == v:
            t[k]=v

print(t)

p = {k:v for x in l for k,v in d.items() if x==v}
print(p)

# # print(sort_dk)
# # print(sort_dv)

# n = 10
# def febo(n):
#     if (0 or 1) in n:
#         return 1
#     else:
#         return febo(n-1)+febo(n-2)
# series= [febo(x) for x in range(n+1)]

# print(series)