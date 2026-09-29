import functools
l=[1,2,3,4]
print(functools.reduce(lambda a,b:a+b,l,0))
print(functools.reduce(lambda a,b:a*b,l,1))
