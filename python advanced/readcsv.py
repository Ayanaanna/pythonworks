# import csv
# f=open('data.csv','w')
# content=[['name','age','place'],['arun',24,'ekm'],['amal',23,'tvm']]
# w=csv.writer(f)
# w.writerows(content)#writes each row to the file
# f.close()


import csv
f=open('data.csv','r')
r=csv.reader(f)
for i in r:
    print(i)

f.close