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
