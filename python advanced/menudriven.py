

# def add():
#     n1=int(input('enter a number'))
#     n2=int(input('enter next number'))
#     s=n1+n2
#     print('addition:',s)

# def sub():
#     n1=int(input('enter a number'))
#     n2=int(input('enter next number'))
#     s=n1-n2
#     print('subtraction:',s)
# def mul():
#     n1=int(input('enter a number'))
#     n2=int(input('enter next number'))
#     s=n1*n2
#     print('multiplication:',s)

# def div():
#     n1=int(input('enter a number'))
#     n2=int(input('enter next number'))
#     s=n1/n2
#     print('multiplication:',s)






# while True:
#     n=int(input("enter choice "))
#     if n==1:
#         add()
#     elif n==2:
#         sub()
#     elif n==3:
#         mul()
#     elif n==4:
#         div()
#     else:
#         exit()



def file_read(): #usage 1
    try:
        filename = input("Enter file name: ")
        f = open(filename, 'r')
        content = f.read()
        print("\nFile Content:")
        print(content)
        f.close()
    except:
        print("file does not exist")


def file_write():
    filename = input("Enter file name: ")
    f = open(filename, 'w')
    content = input("Enter the content: ")
    f.write(content)
    f.close()
    print("Content written successfully.")


def file_append():
    filename = input("Enter file name: ")
    f = open(filename, 'a')
    content = input("Enter the content to append: ")
    f.write(content)
    f.close()
    print("Content appended successfully.")


while True:
    print("\n----- FILE MENU -----")
    print("1. Read File")
    print("2. Write File")
    print("3. Append File")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        file_read()

    elif choice == 2:
        file_write()

    elif choice == 3:
        file_append()

    elif choice == 4:
        print("Program exited.")
        break

    else:
        print("Invalid choice.")

