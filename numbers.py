from random import randint
import math

# 1. Write a program that generates and prints 50 random integers, each between 3 and 6.
def randomNumbers():
    for i in range(50):
        print(randint(3,6))
# randomNumbers()
        

# 2. Write a program that generates a random number, x, between 1 and 50, a random number y
# between 2 and 5, and computes x^y
# .

def square1():
    x = randint(1, 50)
    y = randint(1, 50)
    print(x**y)
# square1()

# 3. Write a program that generates a random number between 1 and 10 and prints your name
# that many times.
def randName(name):
    print(str(name + '\n')*randint(1,10))
# randName('Alfred')

# 4. Write a program that generates a random decimal number between 1 and 10 with two decimal
# places of accuracy. Examples are 1.23, 3.45, 9.80, and 5.00.

# 5. Write a program that generates 50 random numbers such that the first number is between 1
# and 2, the second is between 1 and 3, the third is between 1 and 4, . . . , and the last is between
# 1 and 51.

def mahdRand():
    for i in range(2, 51):
        print(randint(1, i))
# mahdRand()

# 6. Write a program that asks the user to enter two numbers, x and y, and computes |x−y|/(x+y)

def divXY(x:int,y:int):
    print(abs(x-y)/(x+y))
# divXY(2, 8)

# 7. Write a program that asks the user to enter an angle between −180◦ and 180◦. Using an
# expression with the modulo operator, convert the angle to its equivalent between 0
# ◦ and 360◦
# .

def degConverter(angle:int):
    if angle<0:
        print(angle, 'degrees is', angle+360, 'degrees')
    else:
        print(angle, 'degrees')
# degConverter(-90)

# 8. Write a program that asks the user for a number of seconds and prints out how many minutes
# and seconds that is. For instance, 200 seconds is 3 minutes and 20 seconds. [Hint: Use the //
# operator to get minutes and the % operator to get seconds.]

def timeInMinutes(seconds:int):
    mins = seconds//60
    secs = seconds%60
    print(mins, 'mins,', secs, 'secs')
# timeInMinutes(700)

# 9. Write a program that asks the user for an hour between 1 and 12 and for how many hours in
# the future they want to go. Print out what the hour will be that many hours into the future.
# An example is shown below.

# Enter hour: 8
# How many hours ahead? 5
# New hour: 1 o'clock

def hours(hourInitial:int, hourAdded:int):
    hour = hourInitial+hourAdded
    if hour <12:
        print(hour, 'o\'clock')
    elif hour==12 or hour%12==0:
        print('12 o\'clock')
    else:
        print(hour%12, 'o\'clock')
# hours(21,5)
        

# 10. (a) One way to find out the last digit of a number is to mod the number by 10. Write a
# program that asks the user to enter a power. Then find the last digit of 2 raised to that
# power.

# (b) One way to find out the last two digits of a number is to mod the number by 100. Write
# a program that asks the user to enter a power. Then find the last two digits of 2 raised to
# that power.

# (c) Write a program that asks the user to enter a power and how many digits they want.
# Find the last that many digits of 2 raised to the power the user entered.

def ex10(power=1, digits=0):
    if power<7:
        print((2**power)%10)
    else:
        print((2**power)%100)
    print((2**power)%(10**digits))
# ex10(9, 3)

        
# 11. Write a program that asks the user to enter a weight in kilograms. The program should
# convert it to pounds, printing the answer rounded to the nearest tenth of a pound.

# 12. Write a program that asks the user for a number and prints out the factorial of that number.

def fact(x:int):
    print(math.factorial(x))
# fact(6)

# 13. Write a program that asks the user for a number and then prints out the sine, cosine, and
# tangent of that number.

def trigValues(x:int):
    print('sin', x, '=', math.sin(x), 'cos', x, '=', math.cos(x), 'tan', x, '=', math.tan(x))
# trigValues(30)

# 14. Write a program that asks the user to enter an angle in degrees and prints out the sine of that
# angle.

def sineAngle():
    angle = eval(input('Enter an angle in degrees\n'))
    print('sin', angle, '=', math.sin(angle))
# sineAngle()


# 15. Write a program that prints out the sine and cosine of the angles ranging from 0 to 345◦
# in 15◦ increments. Each result should be rounded to 4 decimal places. Sample output is shown
# below:

# 0 --- 0.0 1.0
# 15 --- 0.2588 0.9659
# 30 --- 0.5 0.866
# ...
# 345 --- -0.2588 0.9659

def sinCos0To345():
    for i in range(0, 346, 15):
        print('sin', i, '=', math.sin(i))
        print('cos', i, '=', math.cos(i), '\n')
# sinCos0To345()

# 16. Below is described how to find the date of Easter in any year. Despite its intimidating appearance, this is not a hard problem. Note that bxc is the floor function, which for positive numbers
# just drops the decimal part of the number. For instance b3.14c = 3. The floor function is part
# of the math module.
# C = century (1900’s → C = 19)
# Y = year (all four digits)
# m = (15 + C - [C/4] - [(8C+13)/25]) mod 30
# n = (4 + C- [C/4]) mod 7
# a = Y mod 4
# b = Y mod 7
# c = Y mod 19
# d = (19c + m) mod 30
# e = (2a + 4b + 6d + n) mod 7

# Easter is either March (22+d +e) or April (d +e−9). There is an exception if d = 29 and e = 6.
# In this case, Easter falls one week earlier on April 19. There is another exception if d = 28,
# e = 6, and m = 2, 5, 10, 13, 16, 21, 24, or 39. In this case, Easter falls one week earlier on April
# 18. Write a program that asks the user to enter a year and prints out the date of Easter in that
# year. 

def findEaster(year:int):
    C = eval(str(year)[:2])
    Y = year
    m = (15 + C - math.floor(C/4) - math.floor(((8*C)+13)/25)) % 30
    n = (4 + C - math.floor(C/4)) % 7
    a = Y % 4
    b = Y % 7
    c = Y % 19
    d = ((19*c) + m) % 30
    e = ((2*a) + (4*b) + (6*d) + n) % 7
    march = 22 + d + e
    april = d + e - 9
    easter = 0
    
    if d==29 and e==6:
        easter = 19
        date = 'April ' + str(easter)
    elif d==28 and e==6 and m in [2,5,10,13,16,21,24,39]:
        easter = 18
        date = 'April ' + str(easter)
    elif march > 31 or april < 1:
        easter = april
        date = 'April ' + str(easter)
    else:
        easter = march
        date = 'March ' + str(easter)
        
    print('Easter is on ' + date)
    
# findEaster(2023)
    

# 17. A year is a leap year if it is divisible by 4, except that years divisible by 100 are not leap years
# unless they are also divisible by 400. Ask the user to enter a year, and, using the // operator,
# determine how many leap years there have been between 1600 and that year.

def checkLeapNumber(year:int):
    count = 0
    for i in range(1600, year):
        if i%4==0 and i%100!=0:
            print(count, i)
            count+=1
        elif i%100==0 and i%400==0:
            count+=1
            print(count, i)
        else:
            pass
    # print(count)
# checkLeapNumber(2023)


