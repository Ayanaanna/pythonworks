# strong number
# a number where sum of the factorial of its digit equals number itself is called a strong number

num=145
temp=num
sum=0

while num>0:
    digit=num%10
    fact=1
    for i in range(1,digit+1):
        fact*=i
    sum+=fact
    num//=10

print("strong" if sum==temp else "not strong")