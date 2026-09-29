# global

# x=204
# print("outside",x)

# def f():
#     print("inside",x)
# f()
# local
# def f():
#     x=20
#     print("inside",x)
# f()
# print("outside",x)
def outer():
    x=20 #non local

    def inner():
        y=30
        print("inside inner function",x)

    inner()

    print("insider outer function",y)

outer()

