

# from abc import ABC,abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def get_area(self):
#         pass

#     @abstractmethod
#     def get_perimeter(self):
#         pass


# class Rectangle(Shape):
#     def __init__(self):
#         self.length=int(input("enter the length"))
#         self.breadth=int(input("enter the breadth"))

#     def get_area(self):
#         print("Area",self.length*self.breadth)

#     def get_perimeter(self):
#         print("Perimeter",2*(self.length+self.breadth))


# r=Rectangle()
# r.get_area()
# r.get_perimeter()

# class Square(Shape):
#     def __init__(self):
#         self.s=int(input("enter length of side"))

#     def get_area(self):
#         print("Area",self.s*self.s)

#     def get_perimeter(self):
#         print("perimter",4*self.s)

# s=Square()
# s.get_area()
# s.get_perimeter()

"""
e an abstract class Employee with an abstract method calculate_salary()
# create two subclasses
# -FullTimeEmployee
# -PartTimeEmployee
# Each class should calculate salary differently.
"""

from abc import ABC,abstractmethod
class Employee:

    def __init__(self):
        self.name=input("enter name")
        self.age=int(input("enter age"))
        self.empid=int(input("enter empid"))
    @abstractmethod
    def calculate_salary(self):
        pass

class Fulltimeemployee(Employee):
    def __init__(self):
        super().__init__()
        self.monthlysalary=int(input("enter monthly salary"))

    def calculate_salary(self):
      
        print("monthly salary",self.monthlysalary)

class Parttimeemployee(Employee):
    def __init__(self):
        super().__init__()

        self.rate=int(input("enter hourly rate"))
        self.hours=int(input("enter the hours worked"))

    def calculate_salary(self):
        print("Daily salary",self.rate*self.hours)

s=Fulltimeemployee()
s.calculate_salary()

r=Parttimeemployee()
r.calculate_salary()
