# wap to get product of odd numbers from 1 to 10
# i=1
# prod=1
# while (i<10):
#     if i%2 !=0:
#         prod=prod*i
#     i+=1
# print(prod)

# wap to get sum of numbers which are divisible by 3 and 5 from 1 to 30

# i=1
# sum=0
# while (i<30):
#     if i%3==0 and i%5==0:
#         sum=sum+i
#     i+=1
# print(sum)

# wap to get the sum of even numbers and product of odd numbers from 1 to n

i=1
n=int(input("enterthe number"))
prod=1

sum=0
while(i<=n):
    if i%2==0:
        sum=sum+i
    else:
        prod=prod*i
    i+=1
print(prod)
print(sum)


