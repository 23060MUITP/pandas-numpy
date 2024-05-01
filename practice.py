#Q1
# L=[]
# for i in range(2000,3201):
#     if i%7==0:
#         if i%5!=0:
#             print(i, end=",")
#Q2
# n=int(input("no:"))
# i=1
# f=1
# while i<=n:
#     f=f*i
#     i=i+1
# print(f)
#Q3
# n=int(input())
# dic={}
# for i in range(1,n+1):
#     dic[i]=i*i
#     i=i+1
# print(dic)
#Q4
# n= input()
# p=n.split(',')
# print(p)
# print(tuple(p))
#Q5
# class sstring():
#     def __init__(self):
#         self.g_string = ""
#     def get_string(self):
#         self.g_string=input()
#     def upper_string(self):
#         print(self.g_string.upper())
# i=sstring()
# # i.get_string()
# # i.upper_string()
#Q6
# import math
# def formula(d):
#     c=50
#     h=30
#     q=math.sqrt((2*c*d)//h)
#     return q
# n=input().split(",")
# for i in n:
#     print(round(formula(int(i))), end=",")
#Q8
# lst = input().split(',')
# lst.sort()
# print(",".join(lst)
#Q7 int(num,2)
#11
# i=int(input("no of rows"))
# j=int(input("no of columns"))
# l=[]
# for a in range(0,i):
#     m=[]
#     for b in range(0,j):
#         li=a*b
#         m.append(li)
#     l.append(m)
# print(l)
#Q16
# a=input().split(',')
# l=[]
# for i in a:
#     if (int(i)) % 2 != 0:
#         b=str((int(i))**2)
#         l.append(b)
# print(",".join(l))
i=input().split(" ")
d=0
while True:
    if "D" in i:
        d=d+int(i[i.index("D")+1])
        continue
    else:
        d=d-int(i[i.index("W")+1])
print(d)
