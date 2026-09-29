""" ask th euser to enter a number that is under 20 
.if they enter a number that is 20 or more display the message

 " too high " otherwise "thankyou"
 
 """

num=int(input("enter a number  less  than 20:"))

if num>=20:
    print("too high")
else:
    print("thankyou")