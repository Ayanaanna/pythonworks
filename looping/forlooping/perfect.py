# perfect number
# =====================
# a positive whole number that equals the sum of its proper positive divisors

# wap to check given number perfcet or not
# 8>>>>>>1,4,8,2
# 6>>>>>1,2,3,6

# number=6
# sum=0

# for i in range(1,number):
#     if number%i==0:
#         sum+=i
# if number==sum:
#     print("perfect number")

# wap to print the even factors of the given number

# number=8
# for i in range(1,8):
#     if number%i==0 and i%2==0:
#         print(i)

# wap to get the sum of odd factors of number given

# number=16
# sum=0
# for i in range(1,27):
#     if number%i==0 and i%2!=0:
#         sum+=i
#         print(sum)
# number whose proper divisors add up to less than itself
# for example 16 is a defecient number as sum of its proper divisors(1,2,4,8)=15
# for i in range(1,16):
#     if number%i==0:
#         sum+=i
#         print(sum)
# if sum<number:
#     print("defecient number")

# nested for loop
# perfecr numbers betwwen 1 to 100
# for num in range(1,1000):
#     sum=0
#     for i in range(1,num):
#         if num%i==0:
#             sum+=i
#     if sum==num:
#         print("perfect",num)
# wap to get prime numbers from 1 to 1000

# for num in range(2,1000):
#     for i in range(2,num):
#         if num%i==0:
#             break

#     else:
#         print(f"{num} is prime")
# wap to get armstrong from 1 to 100
# wap to get pallidrome numbers from 1 to 1000

# for num in range(1,1001):
#      # num=1
#      temp=num
#      sum=0
#      length=len(str(num))
#      while num>0:
#           digit=num%10
#           sum+=digit**length
#           num//=10
#      if sum==temp:
#          print(f"{temp} is a armstrong")


for num in range(1,1001):
    rev=0
    temp=num

    while num>0:
        digit=num%10
        rev=rev*10+digit
        num//=10
    if temp==rev:
        print(f"{rev} is a pallidnrome")

          








        


