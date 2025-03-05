logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]

l1 = []
l2 = []

for log in logs:
    x = log.split(" ")
    print(x)
    if x[1].isdigit():
        l1.append(x)
    else:
        l2.append(x)

print(l1)
print(l2)

l2.sort(key= lambda x: x[0])
print(l2)
l2.sort(key= lambda x: x[1:])
print(l2)
print()
for i in range(len(l2)):
    l2[i] = (" ".join(l2[i]))
for i in range(len(l1)):
    l1[i] = (" ".join(l1[i]))
l2.extend(l1)
print(l2)