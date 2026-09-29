# inheritence

# class Parent:
#     def m1(self):
#         print("in parent class method m1 ")
#     def m2(self):
#         print("in parent class method m2")

# p=Parent()
# p.m1()
# p.m2()

# class Child(Parent):

#     def m1(self):
#         super().m1()
#         print("in child class m1")

#     def m3(self):
#         print("in child class m3")
#     pass
# e=Child()
# e.m1()
# e.m2()
# e.m3()


# class Person:
#     def __init__(self):
#         self.name=input("enter name")
#         self.age=int(input("enter age"))

#     def show(self):
#         print(self.name,self.age)

# class Student(Person):
#     def __init__(self):
#         super().__init__()
#         self.rollno=int(input("enter roll no" ))
#         self.course=input("enter course")
#         self.marks=int(input("enter marks"))

#     def show(self):
#         super().show()
#         print(self.rollno,self.marks,self.course)
#     def updatemark(self):
#         self.marks=int(input("enter the mark"))
  

# s=Student()
# s.show()
# s.updatemark()

# class Company:
#     def __init__(self):
#         self.companyname=input("enter the company name")
#         self.location=input("enter the company location")

#     def display_company(self):
#         print("company name",self.companyname,"location",self.location)

# # s=Company()
# # s.display_company()

# class Employee(Company):
#     def __init__(self):
#         super().__init__()
#         self.empid=int(input("enter the emp id"))
#         self.name=input("enter the emp name")
#         self.designation=input("enter the designation")
#         self.salary=int(input("enter the current salary"))

#     def display_details(self):
#         super().display_company()
#         print("empid",self.empid,"emp name",self.name,"designation",self.designation,"current salary",self.salary)

#     def update_salary(self):
#         new_salary=1.1*self.salary
#         print("updated salary",new_salary)

# s=Employee()
# s.display_details()
# s.update_salary()


# class Category:
#     def __init__(self):
#         self.catname=input("enter the category")
#     def show_category(self):
#         print("product category:",self.catname)

# class Product(Category):
#     def __init__(self):
#         super().__init__()
#         self.prodname=input("enter the prod name")
#         self.price=int(input("enter the product price"))
#         self.quantity=int(input("enter the quantity"))

#     def total_price(self):
#         totalprice=self.price*self.quantity
#         print("total price",totalprice)

# s=Product()
# s.show_category()
# s.total_price()

class Hospital:
    def __init__(self):
         self.hos_name=input("enter hospital name")
         self.location=input("enter location")
         self.phone=int(input("enter phone number"))
    def display_hospital(self):
         print("hospital name",self.hos_name,"location",self.location,"phone",self.phone)

class Department:
     def __init__(self):
          
          self.dep_name=input("enter department name")
          self.doc_name=input("enter doctor name")
     def display_department(self):
          print("department name",self.dep_name,"doctor name",self.doc_name)
class Patient(Hospital,Department):
     def __init__(self):
          Hospital.__init__(self)
          Department.__init__(self)
          self.patientname=input("enter patient name")
          self.age=int(input("enter age"))
          self.gender=input("enter gender")
          self.admission_date=input("enter admission date")
          self.bedno=int(input("enter bed no"))
          self.discharge_date=""

     def set_discharge(self):
          self.discharge_date=input("enter new discharge date")

     def full_summary(self):
        Hospital.display_hospital(self)
        Department.display_department(self)
        
        print("patient name",self.patientname,"age",self.age,"gender",self.gender,"admission date",self.admission_date,"bedno",self.bedno,"discahrge date",self.discharge_date)
        if self.set_discharge=="":
                     print("print not yet discahrged")
        else:
                     
                     print("print discahrge date",self.discharge_date)



p=Patient()
p.full_summary()
p.set_discharge()
p.full_summary()