"""
task given an integer ,perform the following conditional actions:

if is odd print " weird" 
if in is even and in th einclusive range 2 to 5 print not weird
if n is even and inclusive range of 6 to 20 print weird
if n is even and greater than 20 print not   eeird

"""

n=int(input("enter number"))
if n%2==0:
    if n>=2 and n<=5:
        print("not weird")
    elif n>=6 and n<=20:
        print("weird")
    elif n>20:
        print("not weird")
else:
    print(" not weird")