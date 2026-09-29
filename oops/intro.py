# # class Person:
# #     def __init__(self):
# #         self.name=input('enter namde')
# #         self.age=int(input("enter age"))
# #     def show(self):
# #         print(self.name,self.age)

# # p1=Person()
# # p1.show()

# # p2=Person()
# # p2.show()

# # define a class named employee with attributes empid,name,age,place,salary designation and methods get salary and showpersonaldetails()


# # create an employee object and call the methods

# # class Employee:
# #     def __init__(self,id,name,age,place,sal,desig):
# #         self.empid=id
# #         self.name=name
# #         self.age=age
# #         self.place=place
# #         self.salary=sal
# #         self.designation=desig

# #     def getsalary(self):
# #         print(self.salary)
# #     def getpersonaldetails(self):
# #         print(self.empid,
# #                 self.name,
# #                 self.age,
# #                 self.place,
# #                 self.designation)

# # pl=Employee(123,'arun',34,'kochi',24000,'engineer')
# # pl.getsalary()
# # pl.getpersonaldetails()

# # define a class named student and attributes rollno,name,mark1,mark2,mark3,mark4 and methods to display roll no and total mark of a student
# # create 2 objects call the methods

# # class Student:
# #     def __init__(self):
# #         self.rollno=int(input("enter rollno"))
# #         self.mark1=int(input("enter mark1"))
# #         self.mark2=int(input("enter mark2"))
# #         self.mark3=int(input("enter mark 3"))

# #     def totalmarks(self):
# #         print("rollno",self.rollno)
# #         print("total marks",self.mark1+self.mark2+self.mark3)

# # e=Student()
# # e.totalmarks()

# # e2=Student()
# # e2.totalmarks()

# # define a class named books with attributes title author,price,pages,language
# # and methods gettitle(),getauthor(),getprice()
# # settitle(),setauthor(),setprice( )

# # class Books:
# #     def __init__(self):
# #         self.title=input("enter title")
# #         self.author=input("enter author")
# #         self.price=int(input("enter price"))
# #         self.pages=int(input("enter pages"))
# #         self.langauge=input("enter langauge")
# #     def gettitle(self):
# #         print(self.title)
        
# #     def getauthor(self):
# #           print(self.author)
# #     def getprice(self):
# #               print(self.price)
# #     def settitle(self):
# #           self.title=input("enter new title")
# #           self.gettitle()

# #     def setauthor(self):
          
# #           self.author=input("enter new author")
# #     def setprice(self):
# #           self.price=input("enter new price")

# # e=Books()
# # e.gettitle()
# # e.getauthor()
# # e.getprice()
# # e.settitle()
# # e.setauthor()
# # e.setprice()


# # class Circle:
# #     def __init__(self):
# #         self.radius=int(input("enter radius"))

# #     def getarea(self):
# #         print("area",3.14*self.radius**2)
# #     def getperimeter(self):
# #         print("perimeter",2*self.radius*3.14)

# # c=Circle()
# # c.getarea()
# # c.getperimeter()

# class Account:
#     def __init__(self):
#         self.accnumber=int(input("enter acc number"))
#         self.accname=input("enter acc name")
#         self.accbalance=int(input("enter acc balance"))

#     def withdraw(self):
#         self.withdrawamt=int(input("enter amount to withdraw"))
#         self.accbalance=self.accbalance-self.withdrawamt
#         print("balance after withdraw:",self.accbalance)
#     def deposit(self):
#         self.depositamt=int(input("enter amount to deposit"))
#         self.accbalance=self.depositamt+self.accbalance
#         print("accbalance after deposit",self.accbalance)
#     def showbalance(self):
#         print("current balance",self.accbalance)
# # e1=Account()
# # # e1.withdraw()
# # # e1.deposit()
# # # e1.showbalance()

# # e2=Account()
# # # e2.withdraw()
# # # e2.deposit()
# # # e2.showbalance()

# # l=[e1,e2]
# # for i in l:
# #     if(i.accnumber==123):
# #         i.showbalance()


# # write a menu driven code for bank operations

# # using classs and list
# # 1.createe a new acc
# # 2.withd9raw
# # 3.deposit
# # 4.showbalance
# # 5.exit




# l=[]
    
# while (1):
#     print("1.create a new acc")
#     print("2.withdrraw")
#     print("3.deposit")
#     print("4.showbalance")
#     print("5.showbalance")


#     ch=int(input("enterchoice"))

#     if ch==1:
#         a=Account()
#         l.append(a)
#         print(l)


#     elif ch==2:
#         number=int(input("enter acc number"))
#         for i in l:
#             if(i.accnumber==number):
#                 i.withdraw()
#                 break
#         else:
#                 print("account doesnt exist")
        
#     elif ch==3:
#         number=int(input("enter accnumber"))
#         for i in l:
#             if(i.accnumber==number):
#                 i.deposit()
#                 break
#         else:
#                 print("doesnt exist")
        
#     elif ch==4:
#         for i in l:
#             i.showbalance()
#     else:
#         exit()


# Write a menu-driven Python program using a class Student
#     to perform the following operations:
# #
# 1Add Student(roll no,name,marks)
# 2Update Marks
# 3Display All Student Details
# 4Search Student by Roll Number
# 5Delete Student
# 6Exit
# Store student records in a list and perform all operations using the student's roll number.

class Student:
    def __init__(self):
        self.rollno=int(input("enter rollno"))
        self.name=input("enter name")
        self.marks=int(input("enter marks"))

    def updatemarks(self):
        newmark=int(input("enter new mark"))
        self.marks=newmark
        print("updated mark",self.marks)
    def displaydetails(self):
        print("studentdetails roll no",self.rollno,"name",self.name,"marks",self.marks)
   
    def deletestudent(self):
        no=int(input("enter the student roll no to delete"))
l=[]
while (1):
    print("1Add Student(roll no,name,marks)")
    print("2Update Marks")
    print("3Display All Student Details")
    print("4Search Student by Roll Number")
    print("5Delete Student")
    print("6Exit")

    ch=int(input("enter choice"))

    if ch==1:
        a=Student()
        l.append(a)
        print(l)

    elif ch==2:
        roll=int(input("enter the roll no to which marks to be updated"))
        for i in l:
            if roll==i.rollno:
                i.updatemarks()
    elif ch==3:
        for i in l:
            i.displaydetails()
    elif ch==4:
         no=int(input("enter rollno to search"))
         for i in l:
              if no==i.rollno:
                print(f"{i.rollno} found")
         else:
             print("not found")
    elif ch==5:
        no=int(input("enter the roll no to delte"))
        for i in l:
            if no==i.rollno:
                l.remove(i)
                print("deleted")
                break
    else:
        exit()

