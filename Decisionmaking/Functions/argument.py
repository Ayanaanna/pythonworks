# arguments types
# ========================

# def sum_a(a,b=8):default argument
#     print(a+b)

# sum_a(4,3)#positional arguments should bother about order of parameters
# sum_a(b=10,a=9)#keyword argument make each value to a specific parameter
# sum_a(a=5) a has assigned bmoved to default argument


# wap to define function to return sum of 3 numbers

# def three(a,b,c):
#     result=a+b+c
#     print(result)

# three(8,7,6)

# return statement

# it is used inside a function to send a value back to place where the function was called


def sum_numbers(*args):#args=(3,7,65,4,3,5)
    sum=0

    for i in args:
        sum+=i

    print(sum)



sum_numbers(2,7,9,5)

sum_numbers(6,8,9)

def details(**kwargs):
    print(kwargs)

details(name="sukumar",age=27,place="kochi")

# list,set,dictionary,tuple
#methods














