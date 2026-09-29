# wap to find the position a specific character in a string
# s='hello world'
# ch='l'
# if ch in s:
#     print("the position of ",ch,"is",s.index(ch))
# else:
#     print("character",ch,"is not present")

# write program to find count of a specific character in a string


# write a program to create a new dictionary where keys are letters and values
# count of each letter
# s='hello world'
# {'h':1,'e':1,'l':2}
# new={}

# for i in s:
#     new[i]=s.count(i)

##Write a program to create a new list with 5 random 3 digit numbers

# new=[]
# import random
# for i in range(5):
#     new=random.randint(1,100)
#     new.append(num)







#write a program to create a 5 digit otp number
# new=[]
# import random
# new=random.randint(10000,99999)







#write a program to find the count of letters,spachelles and digits in a string
# s="hello world 1234"
# count_l=0
# count_d=0
# count_s=0
# for i in s:
#     if i.isalpha():
#         count_l+=1
#     elif i.isspace():
#         count_s+=1
#     elif i.isdigit():
#         count_d+=1
# print(count_l)
# print(count_d)
# print(count_s)


#Write a program to find the position of a specific character in a string

#Write a program to find the count of a specific character in a string


#write a program to create new dictionary where keys are letters and values

#are the count of each letter


#Write a program to create a new list with 5 random 3 digit numbers

#write a program to create a 5 digit otp number


#write a program to find the count of letters,spaces and digits in a string



# ==========================

# write a program to create a new dictionray where keys are words and values re length 

# s='python coding is easy and fun'
# d={}


    

# for i in s.split():
#     d[i]=len(i)
# print(d)

# s=input("enter a string")

# d={}
# for i in s:
#     d[i]=s.count(i)
# print(d)

# import random
# num=[]
# for i in range(5):
#     num.append(random.randint(100,1000))
# print(num)

# import random
# otp=random.randint(10000,99999)
# print(otp)
text=input("enter string")
words=text.split()
d={}
for i in words:
    d[i]=len(i)
print(d)

