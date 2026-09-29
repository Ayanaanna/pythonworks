# wap to reverse the number enter by user

# number=1565
# rev=0
# while number>0:
#     digit=number%10
#     rev=rev*10+digit
#     number=number//10
# print(rev)

# check number number pallindrome or not

n=252
temp=n
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
if rev==temp:
    print("pallindrome")
else:
    print("not a pallinfrome")









































