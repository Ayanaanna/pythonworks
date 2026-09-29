# wap to get the totaldigits in the number given

n=int(input("enter a number"))
# count=0
# while (n>0):
#     n=n//10
#     count+=1
# print(count)

# wap to get count of even digits from the given
# count=0
# while(n>0):

#     digit=n%10
#     if digit%2==0:
#         count+=1
#     n=n//10
# print(count)
# wap to get count of even and count of odd in a given number
even=0
odd=0
while(n>0):
    digit=n%10
    if digit%2==0:
        even+=1
    else:
        odd+=1
    n=n//10
print(odd)
print(even)

