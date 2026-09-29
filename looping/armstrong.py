# Armstrong number
# ================================
# check the given is a armstrong or not

n=223
temp=n
while n>0:
    digit=n%10
    sum=+digit**3
    
    n=n//10
if sum==temp:
    print("armstrong") 
else:
    print("not armstrong")