# class Counter:
#     def __init__(self):
#         self.value=10
#     def __add__(self, other):
#         if isinstance(other, Counter):
#             print(f"{self.__class__.__name__}")
#             return self.value + other.value
            
#         else:
          
#             raise ValueError(f"other is not object of '{self.__class__.__name__}' calss")
        
#     def __repr__(self):
#         return f"this is '{self.__class__.__name__}' class."
    
# class Runner(Counter):
#     def __init__(self, power):
#         super().__init__()
#         self.power= self.value*power

#     def __repr__(self):
#         return f"{super().__repr__()} with {self.power} power." 



# class Point2D():
#     def __init__(self,x,y):
#         print("setting x")
#         self.x = x
#         print("setting y")
#         self.y = y 
#     @property
#     def x(self):
#         print("gettng x")
#         return self._x
#     @x.setter
#     def x(self, value):
#         print("x setter called")
#         self._x = int(value)
#     @property
#     def y(self):
#         print("gettng y")
#         return self._y
#     @y.setter
#     def y(self, value):
#         print("y setter called")
#         self._y = int(value)

# p = Point2D(3,4)

# print(p.x)
# print(p._x)

# print(dir(p))
# print(p.__dict__)
    
# # c1 = Counter()
# # print(c1)
# # r1= Runner(3)
# # print(r1)



# if __name__ == '__main__':
#     n = int(input().strip())

# def getMaxDeletions(s):
#     right= s.count('R')
#     left= s.count('L')
#     up= s.count('U')
#     down= s.count('D')
    
#     if up>down:
#         ver_move=up-down
#     else:
#         ver_move=down-up
#     if left>right:
#         hor_move=left-right
#     else:
#         hor_move=right-left
#     min_move= ver_move + hor_move
#     del_move= len(s)-min_move
    
# px = [7,1,2,5]
# def maxDifference(px):

    # min_price = px[0]
    # spread= 0
    # result= 0

    # for i in range(1,len(px)):
    #     for j in range(i):
    #         if px[i]>px[j]:
    #             spread = px[i]-px[j]
    #             result= spread if spread>result else result
    #         else:
    #             return -1
    # return result

#     if not px or len(px)<2:
#         return -1
#     min_price= px[0]
#     max_spread= -1
#     for p in px[1:]:
#         spread = p - min_price
#         max_spread = max(max_spread, spread)
#         min_price= min(min_price, p)

#     return max_spread if max_spread>0 else -1

# print(maxDifference(px))

# logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
# Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]

# l1 = []
# l2 = []

# for log in logs:
#     x = log.split(" ")
#     print(x)
#     if x[1].isdigit():
#         l1.append(x)
#     else:
#         l2.append(x)

# print(l1)
# print(l2)

# l2.sort(key= lambda x: x[0])
# print(l2)
# l2.sort(key= lambda x: x[1:])
# print(l2)
# print()
# for i in range(len(l2)):
#     l2[i] = (" ".join(l2[i]))
# for i in range(len(l1)):
#     l1[i] = (" ".join(l1[i]))
# l2.extend(l1)
# print(l2)


# from copy import deepcopy

# nums = [-2,1,-3,4,-1,2,1,-5,4]

# total= nums[0]
# max_sum= nums[0]
# for x in nums[1:]:
#     total= max(x, total+x)
#     max_sum= max(max_sum, total)
# print(max_sum)
# s = 0
# l=[]
# m= []
# ad = None
# b_ad= None

# for x in range(s, len(nums)):
#     if nums[x] <0:
#             pass
#     else:
#         for y in range(s, len(nums)):
#             l.append(nums[y])
#             ad = sum(l)
#             b_ad= ad if b_ad== None else b_ad
#             if ad > b_ad:
#                 m = deepcopy(l) 
#                 b_ad=ad
#     print(l)
#     s = s+1
#     l = []

# print(b_ad, m)


# vowel = ['a', 'e', 'i', 'o', 'u']
# word = "programming"

# x= [x for x in word if x in vowel]
# y= [x for x in word if x not in vowel]

# print(x, len(x))
# print(set(y), len(set(y)))

# word = "python"
# character = "p"

# c = [x for x in word if x == character]
# print(c, len(c))

# fib= [0,1]

# for i in range(5):
#     fib.append(fib[-1]+fib[-2])

# print(fib)

# y = ','.join(str(e) for e in fib)
# print(y)

# numberList = [15, 85, 35, 89, 125]

# print(max(numberList))
# print(min(numberList))

# numList = [1, 2, 3, 4, 5]
# i = int(len(numList)/2)
# print(numList[i])

# lst = ["P", "Y", "T", "H", "O", "N"]
# x = ''.join(lst)
# print(x)

# lst1 = [1, 2, 3]
# lst2 = [4, 5, 6] 
# lst1.extend(lst2)
# print(lst1)

# x = [sum(x) for x in zip(lst1,lst2)]
# print(x)


# str1 = "Listen"
# str2 = "Silent"

# str1= list(str1.upper())
# str2= list(str2.upper())
# str2.sort()
# str1.sort()

# if str1== str2:
#     print("its anagram.")
# else:
#     print("not anagram.")


# str1 = "Kayak".lower()
# str2 = "kayak".lower()

# str2= str2[::-1]
# if str1== str2:
#     print("its palandrom")
# else:
#     print("not palandrom.")


# string = "P r ogramm in g "
# c = 0
# for i in string:
#     if i ==' ':
#         c = c+1
# print(c)

# print(string.count(' '))

# l = [1,2,3,1,2,3]

# print(l.count(1))

# import re

# txt = "The rain in Spain"
# name = 'Python is 1'



# x = re.findall("ai", txt)
# print(x)

# txt = "The rain in Spain"
# x = re.split("\s", txt)
# print(x) 


# txt = "The rain in Spain"
# x = re.sub("\s", "9", txt)
# print(x) 

# n=5
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ", end="")
#     for j in range(i+1):
#         print('*', end=" ")
#     print()


# for i in range(n):  
#     for j in range(i):
#         print(" ",end="")
#     for j in range(n-i,0, -1):
#         print('*', end=' ')
#     print()


# n = 5
# f = 1
# for n in range(1,n+1):
#     f =f*n
# print(f)


# i=  [100, 4, 200, 1, 3, 2]
# i = sorted(list(set(i)))
# print(i)

# l = 0
# f=[]
# fn=[]
# for x in range(len(i)):
#     if i[x]-1 not in i:
#         f.append(i[x])
#         le=1
#         while i[x]+le in i:
#             f.append(i[x]+le)
#             fn = f if len(f) > len(fn) else fn
#             le= le+1
#             l = max(l, le)
#         f= []

# print(l)
# print(fn)

# r = [1,0,2]
# # r=[1,2,2]
# c=1
# s=0
# for i in range(len(r)):
#     print(i,s)
#     if i < (len(r)-1):
#         if i==0:
#             if r[i]>r[i+1]:
#                 c = c+1
#                 s = s+c
#             elif r[i]<r[i+1]:
#                 c=1
#                 s=s+c        
#             else:
#                 c = c-1
#                 s= s+c
#         if i>0:
#             if r[i]>r[i+1]:
#                 c = c+1
#                 s = s+c
#             elif r[i]<r[i+1]:
#                 if r[i]>r[i-1]:
#                     c =c+1
#                     s=s+c
#                 else:
#                     c=1
#                     s=s+c        
#             else:
#                 if r[i]>r[i-1]:
#                     c= c+1
#                     s=s+c
#                 else:
#                     c = c-1
#                     s= s+c
#     if i == (len(r)-1):
#         print(i,s)
#         if r[i]>r[i-1]:
#             c = c+1
#             s = s+c
#         elif r[i]<r[i-1]:
#             c=c
#             s=s+c        
#         else:
#             c = c-1
#             s= s+c

# print(s)

        
# def days():
#     day = ['S','M','T','W','Tr','F','St']
#     for i in day:
#         yield i

# res = days()
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))


days = ['S','M','T','W','Tr','F','St'] 
i = ''.join(days)
print(i)