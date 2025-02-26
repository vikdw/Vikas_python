import re

# ip=r'(?:\d{1,3}\.\d{1,3}\.\d{1,3}\.\d+)'
# URL=r'(?:\d{1,2}:\d{1,2}:\d{1,2})(?:\sINFO\s+:\.+URL:\s)(.*)'
# rl =[ip,URL]
# d ={}


# with open("sample.log", 'r') as f:
#     file = f.read()
#     s =re.search(ip, file)
#     print(s, s.span(),)
    # for r in rl:
        # pattern= re.compile(r)
        # matches=pattern.findall(file)
        # print(matches)
        # d[r]=matches
# print(d)

# print(re.search(ip,))

string="www.google.com www.link.com"
r=r'(www\.)([a-zA-Z0-9]+)(\.\w{1,4})'

pattern= re.compile(r)

m = pattern.finditer(string)
print(m)
for x in m:
    print(x.group(2))


m = pattern.findall(string)
print(m)

repl=r'\1linkedin\3'
replcasedstring= re.sub(r,repl, string)

print(replcasedstring)

p1=pattern.sub(repl,string)
print(p1)

# p2= pattern.