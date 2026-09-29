# factorialn+


# for i in range(2,7):
#     fact=1
#     for j in range(1,i+1):
#         fact*=j
#     print(fact)

# wap to get sum of facctors of the given number
fact=1
sum=0
num=9
for i in range(1,num+1):
    if num%i==0:
        sum=sum+i
        print(sum)



