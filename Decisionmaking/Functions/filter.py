# # l=[1,2,3,4,5,6,7,8,9,10]
# # print(list(map(lambda x:x%2==0,l)))>>>>>>>>>>[False, True, False, True, False, True, False, True, False, True]
# # print(list(filter(lambda x:x%2==0,l)))


# l=[23,65,89,12,20,33,85,40]

# # print(list(filter(lambda x:x>50,l)))

# # print(list(filter(lambda x:x<50 and x%2==0,l)))
# fruits=['apple','orange','pineapple','grapes','avacado']
# print(list(filter(lambda x:len(x)>5,fruits)))



# def newsquare(l):
#      return l**2




# print(newsquare(5))

# s=lambda a:a.get('name')

# d = {
#     "name": "ayana",
#     "salary": 1000
# }
# print(s(d))
# l = [
#     {'empid':100,'name':'arun','salary':20000,'email':'arun@gmail.com'},
#     {'empid':101,'name':'amal','salary':25000,'email':'amal@gmail.com'},
#     {'empid':102,'name':'anu','salary':30000,'email':'anu@gmail.com'}
# ]

# print(list(map(lambda x:x['empid'],l)))

# l = [10, 45, 23, 89, 12]
# def maxnum(l):
#     return max(l)
# print(maxnum(l))
l = ['red','green','blue']
print(list(map(lambda x:len(x),l)))