"""

Set the total to 0 to start with. While the total is 50 or less, ask 
the user to input a number. Add that number to the total and 
print the message “The total is… [total]”. Stop the loop when 
the total is over 50.
"""



total=0
while(total<=50):
    n=int(input('enter a number from 0 to 50'))
    total=total+n
print(f"total is {total}")

