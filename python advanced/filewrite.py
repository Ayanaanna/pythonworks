# write
f=open('k.txt','w')


# write(string)
# f.write("hello\n")
# f.write("python\n")
# f.write("""
# Technology has become an important part of our daily lives.
#  It helps us communicate with people, learn new skills, and complete tasks more efficiently. 
#  Students use technology for online learning, research, and project work, while businesses rely on it to improve productivity. 
#  Although technology offers many benefits, it is also important to use it responsibly and maintain a healthy balance between screen time and real-life activities.


# """)
f.writelines(['hello\n','python\n','hi\n','world\n'])
f.close()