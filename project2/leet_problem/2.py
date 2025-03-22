s = 'abcabcbbab'
# s ='bbbbb'
c=''
old_c=''
l =0
sum = 0
old_sum= 0

for x in s:
    while x in c:
        c = c[1:]
    c= c+x
    old_c= c if len(c)> len(old_c) else old_c

    sum = len(c) if len(c)> old_sum else old_sum
    old_sum=sum




# for r in range(len(s)):
#     while s[r] in c:
#         c.remove(s[l])
#         l = l+1
#     c.add(s[r])
#     sum = max(sum, r-l+1)

print(c, sum, old_c)

