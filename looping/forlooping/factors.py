# wap to get the factors of the given numner

"""
8>>>>>> 1,2,4,8 >> range(1,9)>1,2,3,4,5,6,7,8


"""

number=10
for i in range(1,number+1):
    if number%i==0:
        print(i)