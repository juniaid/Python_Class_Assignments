import sys
import datetime

a = '''Twinkle, twinkle, little star,
            How I wonder what you are!
                  Up above the world so high,
                  Like a diamond in the sky.
        Twinkle, twinkle, little star,
             How I wonder what you are'''

print(a)

"Python Version"

version = str(sys.version)

print('The Version of Python is'+ ' ' + version )

"Current date"

date = datetime.datetime.now()

print(date)

"Area of a circle"

for_pie = 3.142
r = int(input('Please enter the radius for area '))
area = (for_pie *r**2)
area1 = round(area)
area2 = str(area1)
print('The Area of given raius is '+' '+area2)

"Print first and last name reverse with Space"

first_name = input("Enter your first name ")
last_name = input("Enter your last name ")
full_name = first_name[::-1]+' '+last_name[::-1]
print(full_name)


"take two inputs from users and print it"

val1 = int(input('Enter the first number for addition'))

val2 = int(input('Enter the second number for addition'))


addition = str(val1 + val2)
print('The addition of two numbers is'+' '+ addition)
