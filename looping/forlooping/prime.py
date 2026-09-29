# prime number

n=9
for i in range(2,n):
    if n%i==0:
        print("its not prime")
        break
else:
    print("its prime")