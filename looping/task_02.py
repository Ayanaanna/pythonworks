"""
Ask the user to enter 
a number. Keep 
asking until they enter 
a value over 5 and 
then display the 
message “The last 
number you entered 
was a [number]” and 
stop the program.
"""
# Keep asking the user until they enter a number greater than 5

number = int(input("Enter a number: "))

while (number <= 5):
    number = int(input("Enter a number greater than 5: "))

print("The last number you entered was a", number)
  