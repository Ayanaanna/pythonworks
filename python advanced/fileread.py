# read
# f=open('k.txt','r')
# s=f.readlines()
# print(len(s))

# s=f.read()

# print(s)

# s=f.readlines()

# print(s)

# f.close()

# # #write a program to read a text file and displays the number of lines in a file


f=open('k.txt','r')
# s=f.readlines()
# print(len(s))
# # #write a program to display the number of words in a file
# s=f.read()
# w=s.split()
# print(len(w))
# # #write a program to update the second line in a file


# s=f.readlines()
# s[1]='vscode\n'

# f=open('k.txt','w')
# f.writelines(s)
# f.close()




# # #write a program to display the last 5 lines in a file
f = open("k.txt", "r")

# s = f.readlines()

# print(s[-5:])

# f.close()

#
# #program to search a particular word in a file
s=f.readlines()
# w='python'
# if w in s:
#     print("word found")
# else:
#     print("not found")

# #find the number of letters,digits,and spaces in a file
# l=0
# d=0
# a=0
# for i in s:
#     if i.isalpha():
#         l+=1
#     elif i.isdigit():
#         d+=1
#     elif i.isspace():
#         a+=1
# print(l)
# print(d)
# print(a)







#reverse the lines in a file
print(s[::-1])



# A file total_students.txt contains the names of all students in a class,
# and a file passed_students.txt contains the names of students who passed.txt the exam.
# Write a Python program to:
# Read the names from both files.
# # Find the students who did not pass.
# # Write their names to a new file named failed_students.txt, one name per line.
# #

