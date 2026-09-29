# # # Q.Write Python Programs Using map(), filter(), or reduce()
# # # 1.Capitalize all names in a list
# # names = ['alin', 'arun', 'anu']

# # print(list(map(lambda x:x.capitalize(),names)))

# # # 2.Append "@gmail.com" to a list of usernames

# # print(list(map(lambda x:x+'@gmail.com',names)))

# # # 3.Filter out all empty strings from a list
# # # words = ['hello', ' ', 'world', ' ', 'python']


# # words = ['hello', ' ', 'world', ' ', 'python']

# # print(list(filter(lambda x: x.strip() != "", words)))

# # # 4.Filter names that start with the letter 'A'
# # names = ['Anu', 'Neenu', 'Arun', 'Ravi']
# # print(list(filter(lambda x:x[0]=='A', names)))

# # # 5.Concatenate all strings in a list
# # words = ['Python', 'is', 'fun']

# # from functools import reduce

# # words = ['Python', 'is', 'fun']

# # result = reduce(lambda x, y: x +y, words)

# # print(result)

# # # 6.Multiply all numbers in a list
# # nums = [2, 3, 4]

# # import functools
# # print(functools.reduce(lambda x,y:x*y,nums,1))


# # # 7.Extract First Character of Each Word
# # words = ["apple", "banana", "cherry"]
# # print(list(map(lambda x:x[0],words)))

# # # 8.Add 10 to Each Number
# # nums = [5, 10, 15]
# # print(list(map(lambda x:x+10,nums)))

# # # 9.Given a list
# # l=[12,-4,78,-34,90,45,16,26,-2,-11,3]
# # #     # #Sum of positive even numbers

# # import functools
# # print(functools.reduce(lambda x,y:x+y,filter(lambda n:n>0 and n%2==0,l),0))


# # #     # #Sum of Positive Odd numbers
# # import functools
# # print(functools.reduce(lambda x,y:x+y,filter(lambda n:n>0 and n%2!=0,l),0))
# # # #     # #Sum of Negative  odd numbers
# # import functools
# # print(functools.reduce(lambda x,y:x+y,filter(lambda n:n<0 and n%2!=0,l),0))
# # # #     # #Sum of Negatve Even numbers
# # import functools
# # print(functools.reduce(lambda x,y:x+y,filter(lambda n:n<0 and n%2==0,l),0))
# # # #     # #Count of Positive numbers
# # print(functools.reduce(lambda x,_:x+1,map(lambda n:n>0,l),0))

# # # 10.Given a list nums = ["1", "2", "3", "4"]
# # # # Convert all Strings to Integers [1,2,3,4]

# # nums = ["1", "2", "3", "4"]
# # print(list(map(lambda x: int(x),nums)))

# # # 11
# # p= [{'name':'laptop','price':50000},
# #     {'name':'phone','price':20000},
# #     {'name':'watch','price':3000},
# #     {'name':'Tablet','price':25000}]

# # #print list of product names in Uppercase

# # print(list(map(lambda x:x['name'].upper(),p)))

# # # #print products with price greater than 10000
# # print(list(filter(lambda x:x['price']>10000,p) ))

# # #Find the total price of all products

# # import functools
# # print(functools.reduce(lambda x,y:x+y['price'],p,0))







# l = [1,2,3,4]
# words = ['Python','is','fun']
# nums = ["1","2","3","4"]

# # from functools import reduce
# # print(reduce(lambda x,y:x*y, nums,1))

# p = [
#     {'name':'laptop','price':50000},
#     {'name':'phone','price':20000},
#     {'name':'watch','price':3000},
#     {'name':'Tablet','price':25000}
# ]

# l = [12,-4,78,-34,90,45,16,26,-2,-11,3]
# from functools import reduce
# print(reduce(lambda x,_:x+1,filter(lambda x:x>0,l),0))

# print(list(filter(lambda x:x['price']>10000, p)))




















# def numbers(l):
#     even=0
#     odd=0
#     greater=0
#     for i in l:
#         if i%2==0:
#             even+=1
         

#         else:
#             odd+=1
          
        
#         if i>50:
#             greater+=1



        

#     print('even',even)
#     print('odd',odd)
#     print('greater',greater)

# l = [23,56,12,78,98,89,31,67]
# print(numbers(l))


# l = [1,1,2,3,4,5,5,5,6,7]
# d={}
# count=0

# for i in l:


# print(d)

# l = [12,-4,78,-34,90,45,16,26,-2,-11,3]
# from functools import reduce
# print('positive even sum',reduce(lambda x,y:x+y,filter(lambda a:a>0 and a%2==0,l),0))
# print('positive odd sum',reduce(lambda x,y:x+y,filter(lambda a:a>0 and a%2!=0,l),0))
# print('positive even sum',reduce(lambda x,y:x+y,filter(lambda a:a<0 and a%2==0,l),0))
# print('positive even sum',reduce(lambda x,y:x+y,filter(lambda a:a<0 and a%2!=0,l),0))

# rectangle
# for i in range(1,6):
#     for j in range(1,10):
#         print(i*j,end=" ")
#     print()

# l = [[1,2,3],[4,5,6],[7,8,9]]
# sum=0
# count=0
# for i in l:
#     for j in i:
#         if j%2==0:
#             count+=1
# print(count)


"""
1 1
1 2
2 1
2 2
3 1
3 2


2.

* * *
* * *
* * *


"""

# 3
# for i in range(1,6):
#     for j in range(i):
#         print('*',end=" ")
#     print()

# 4
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# # 5
# 1 1
# 2 2
# 3 3

# 6
# 1 1
# 1 3
# 2 1
# 2 3
# 3 1
# 3 3

# 7

# l = [[10,20,30],[40,50,60],[70,80,90]]
# sum=0

# for i in l:
#     for j in i:
#         sum+=j
# print(sum)
# 8

# l = [[1,2,3],[4,5,6],[7,8,9]]
# count_even=0
# count_odd=0
# for i in l:
#     for j in i:
#         if j%2==0:
#             count_even+=1
#         else:
#             count_odd+=1
# print(count_odd)
# print(count_even)

# 9
# for i in range(1,6):
#     for j in range(i,6):
#         print('*',end=" ")
#     print()
# 10

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end="")
#     print()
# #


# l=[1,2,3,4,5,6,7,8,9]
# print([x**2 for x in l if x%2==0])

# l = [1,2,3,4,5,6]
# print([x**3 for x in l if x%2!=0])

# colors = ['red','green','blue','yellow','black']
# print([len(x) for x in colors])

# l = [-10,20,-30,40,50,-60]
# print([x for x in l if x>0])
#5  didnt get
# d={}
# print({})

# # 6
# l = [1,2,3,4,5,6,7,8,9,10]
# print({l[i]==i**3 for i in l if i%2==0})

# 8

# names = ['Anu','Arun','Neenu','Amal','Ravi']
# print([x for x in names if x[0]=='A'])

# words = ['python','java','c','javascript','go']
# print(words[x]=={len(x) for x in words})

# l = [1,2,3,4,5,6,7,8,9,10]
# print({x:x**3 for x in l if x%2==0})

# words = ['python','java','c','javascript','go']
# print({x:len(x) for x in words})

# l = [12,-5,8,-10,15,20,-3,7]
# print(i for i in l if i>0 i else i<0)


# 1
# hello
# 2
# 15

# 3
# def cuben(x):
#     return x**3
# n=cuben(2)
# print(n)

# 4




"""
1.b
2.a
3.b
4.b
5.d
6.a
7.b
8.a
9.b
10.b
11.b
12.a
13.b
14.a
15.b
16.a
17.c
18.d
19.b
20.c
21.c
22.b
23.b
24.b
25.a
26.b
27.c
28.b
29.b
30.c
31.b
32.b
33.c
34.25
35.b
36.b
37.b
38.c
39.b
40.b



"""

# coding
# 1
# for i in range(1,501):
#     sum=0
#     org=i
#     for j in range(1,i):
#         if i%j==0:
#             sum+=j

#     if sum==org:
#         print("perfcet",i)

# l = [12, 45, 12, 67, 89, 45, 23, 67, 12, 90]
# dict={}
# for i in l:
#     dict[i]=l.count(i)
  



# print(dict)
# print(max(dict.values()))

# for i,j in dict.items():
#     if i>50:
#         print(i,j)




for i in range(1,6):
    for j in range(1,i+1):
            if j%2==0:
                 continue
            print(j,end="")
    print()


