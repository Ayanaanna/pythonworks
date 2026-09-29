# wap to get the sum of even digits of the number
n=1445
# sum=0
# while (n>0):
#     digit=n%10
#     if digit%2==0:
#         sum+=digit
#     n=n//10
# print(sum)

# wap to get the product of odd digits of a number

prod=1
while (n>0):
    digit=n%10
    if digit%2!=0:
        prod*=digit
    n=n//10
print(prod)


