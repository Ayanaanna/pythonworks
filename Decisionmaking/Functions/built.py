"""
len()
list()
clear()
copy()
insert()
pop(index)
remove(element)


list
=======
append: add single elemnet
extend:add sequence of element
insert:syntax:insert(index,element)
to remove the element and add another:l[index]=element
index:return the position

count:
reverse:reverse elements also used:l[::-1]
sort:arrange elements in order default ascending
remove:remove elements
diff bet pop and remove:pop return value remove doesnt
copy:\
clear:remove elements
max:maximum element
min:

given a list

questions
==========
l=[1,1,2,3,4,5,5,5,6,7]
create a new dictionary where keys are numbers and values are count of each number
given list=[34,12,56,89,90,11]
find the second largest elemnet
find largest
find smallest
find second smallest

data types:
====================

set
=====

s={1,2,3,4}
immutable
set()
len()
add()
to add new elements
=======================
add():add one element
update()multiple element
update(sequence) remove duplicates and update
to remove elements
===================\
remove(element)
discard(element)
pop()
===
removes and return random element


union()
intersection()
difference()
symmetric_ difference() opposite of intersection


dictionary
=============================

d={key:value,key:value}
d={'name':'arun','age':23,'place':'ekm'}
dict(sequence)
len()
values()
keys()
items()
get()
update(dictionary)
pop(keyname)
popitem()
get()




"""

# l=[1,1,2,3,4,5,5,5,6,7]
# d={}
# for i in l:
#   print(list.pop())  d[i]=l.count(i)
# print(d)

# list=[34,12,56,89,90,11]
# list.sort()
# print("second max",list[-2])
# print("second min",list[1])
# list.pop()

# print(max(list))
# largest=list[0]
# print(min(list))

# l=[["arun",23,40000],['amal',24,500000],['anu',27,300000]]
# s=[]
# age=[]
# n=[]
# for i in l:
#     s.append(i[2])
#     age.append(i[1])
#     n.append(i[0])
# for i in l:
#     age.append(i[1])
# for i in l:
#     n.append(i[0])



# print(max(s))
# print(n)
# print(min(age))



# 1.Given a list l=[1,1,1,2,3,3,4,5]

# remove duplicates from list


# 2.Given a list l=[1,,1,1,2,3,3,4,5]

# remove duplicates without set()

# 3.Given two lists

# l1=[23,45,78,90,12,74]
# l2=[45,89,23,56,34]

# print common elelments

# l=[1,1,1,2,3,3,4,5]
# s=set(l)
# print(s)
# new=[]
# for i in l:
#     if i not in s:
#         new.append(i)
# print(new)

# l1=[23,45,78,90,12,74]
# l2=[45,89,23,56,34]
# s1=set(l1)
# s2=set(l2)
# print(s1.intersection(s2))

# l=[1,2,2,3,3,4,5]
# new=[]
# for i in l:
#     if i not in new:
#         new.append(i)
# print(new)

"""

Define a function that takes a list of numbers

as argument and print the count of even numbers,
odd numbers and numbers whose value greater than 50

l=[23,56,12,78,98,89,31,67]

"""
# l=[23,56,12,78,98,89,31,67]
# def countnum():
#     evn=0
#     odd=0
#     greater=0

#     for i in l:
#         if i%2==0:
#             evn+=1
           
#         else:
#             odd+=1
#         if i>50:
#             greater+=1
#     print("even count",evn)
#     print("odd count",odd)
#     print(greater)


# countnum()

# ====================================

# l=[1,1,2,3,4,5,5,5,6,7]
# d={}
# for i in l:
#     d[i]=l.count(i)
# print(d)

# l = [34,12,56,89,90,11]
# l.sort()
# print(l[1])

# l = [1,1,1,2,3,3,4,5]
# new=[]

# for i in l:
#     if i not in new:
#         new.append(i)
# print(new)

# l1 = [23,45,78,90,12,74]
# l2 = [45,89,23,56,34]
# l3=[]

# for i in l1:
#     if i in l2:
# print()

# l = [23,56,12,78,98,89,31,67]
# count=0
# for i in l:
#     if i>50:
#         count+=1
# print(count)




        






