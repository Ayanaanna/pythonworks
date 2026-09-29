# wap to get mark from the student
# if the mark is above 90 less than or equal to 100 "A grade"
# if the mark above 80 less than oru equal to 90 "B grade"
# if mark above or equal to 60 less than or equal to 80 "c grade"



mark=int(input("enter the mark"))

if mark>90:
    if mark<=100:
        print("A grade")
if mark>80:
    if mark<=90:
        print("B grade")
if mark>=60:
    if mark <=80:
        print("C grade")
else:
    print("sorry u are failed")