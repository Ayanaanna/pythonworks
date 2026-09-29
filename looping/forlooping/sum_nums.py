# wap to get the count of numbers divisible by 7 from 1 to 50

count=0
for i in range(1,50):
    if i%7==0:
        print(i)
        count+=1
print("count is",count)