# f=open('k.txt','a+')
# print(f.tell())
# f.write('python')
# print(f.tell())
# f.seek(0)
# print(f.read())
# print(f.tell())

# f.close()

import os
os.remove('k.txt')
print('file is cleared')