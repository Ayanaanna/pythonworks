# write

f=open("data.json",'w')
content=[{'name':'arun','age':'23'},{'name':'amal','age':24}]
import json
json.dump(content,f)


# read
f=open("data.json",'r')
import json
content=json.load(f)
print(content[0]['name'],content[0]['age'])

f.close()

