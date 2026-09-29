"""
ask the users age if they are 18 or more display you can vote
if they are 17 display dispaly you can learn to drive
if they are 16 display you can buy a lottery ticket
if under 16 display you can trick or -or-treating
"""

num=int(input("enter age"))

if num >= 18:
    print("you can vote")

elif num==17:
    print("you can learn to drive")
elif num==16:
    print("you can buy a lottery ticket")
else:
    print("you can go trick or treating")
