from random import randint


# 1. Write a program that asks the user to enter a length in centimeters. If the user enters a negative
# length, the program should tell the user that the entry is invalid. Otherwise, the program
# should convert the length to inches and print out the result. There are 2.54 centimeters in an
# inch.

def cmToInches():
    cmValue = eval(input('Enter length in centimeter '))
    if cmValue < 0:
        print('Invalid Entry.\nNumber must be positive')
        cmToInches()
    else:
        inchValue = 2.54 * cmValue
        print(str(cmValue)+'cm = '+str(inchValue)+'inches')
# cmToInches()

# 2. Ask the user for a temperature. Then ask them what units, Celsius or Fahrenheit, the temperature 
# is in. Your program should convert the temperature to the other unit. The conversions
# are F = (9/5)*C +32 and C = (5/9)*(F-32)
def convertTemperature():
    def f_c(temp1):
        temp2 = (5/9)*(temp1-32)
        print(str(temp1) + 'deg F = ' + str(temp2) + 'deg C')
    def c_f(temp1):
        temp2 = (9/5)*temp1 +32
        print(str(temp1) + 'deg C = ' + str(temp2) + 'deg F')
    temp1 = eval(input('Enter Temperature '))
    unit = input('Enter unit: C or F ')
    if 'c' in unit or 'C' in unit:
        c_f(temp1)
    elif 'f' in unit or 'F' in unit:
        f_c(temp1)
    else: 
        pass
# convertTemperature()
        


# 3. Ask the user to enter a temperature in Celsius. The program should print a message based
# on the temperature:
# • If the temperature is less than -273.15, print that the temperature is invalid because it is
# below absolute zero.
# • If it is exactly -273.15, print that the temperature is absolute 0.
# • If the temperature is between -273.15 and 0, print that the temperature is below freezing.
# • If it is 0, print that the temperature is at the freezing point.
# • If it is between 0 and 100, print that the temperature is in the normal range.
# • If it is 100, print that the temperature is at the boiling point.
# • If it is above 100, print that the temperature is above the boiling point.

def checkTempRange(temp:int):
    if temp<-273.15:
        print('Invalid. Temperature is below Absolute Zero')
    elif temp==-273.15:
        print('Temperature is at Absolute Zero')
    elif -273.15<temp<0:
        print('Temperature is below Freezing')
    elif temp==0:
        print('Temperature is at Freezing Point')
    elif 0<temp<100:
        print('Temperature is within normal range')
    elif temp==100:
        print('Temperature is at Boiling Point')
    elif temp>100:
        print('Temperature is above Boiling Point')
    else:
        pass
# checkTempRange(-150)


# 4. Write a program that asks the user how many credits they have taken. If they have taken 23
# or less, print that the student is a freshman. If they have taken between 24 and 53, print that
# they are a sophomore. The range for juniors is 54 to 83, and for seniors it is 84 and over.



# 5. Generate a random number between 1 and 10. Ask the user to guess the number and print a
# message based on whether they get it right or not.


# 6. A store charges $12 per item if you buy less than 10 items. If you buy between 10 and 99
# items, the cost is $10 per item. If you buy 100 or more items, the cost is $7 per item. Write a
# program that asks the user how many items they are buying and prints the total cost.

def calcCharge(quantity:int):
    if quantity<10:
        price = 12
    elif quantity<100:
        price = 10
    else:
        price = 7
    print('Total price is ' + str(quantity*price))
# calcCharge(120)


# 7. Write a program that asks the user for two numbers and prints Close if the numbers are
# within .001 of each other and Not close otherwise.

def checkPointClose(num1, num2):
    diff = abs(num1-num2)
    if diff <=0.001 and diff!=0:
        print('Close')
    elif diff==0:
        print('Same')
    else:
        print('Not Close')

# checkPointClose(12, 12.0009)


# 8. A year is a leap year if it is divisible by 4, except that years divisible by 100 are not leap years
# unless they are also divisible by 400. Write a program that asks the user for a year and prints
# out whether it is a leap year or not.

def checkLeapYear(year:int):
    if year%4==0 and year%100!=0:
        print('Leap Year')
    elif year%100==0 and year%400==0:
        print('Leap Year')
    else:
        print('Not Leap Year')
# checkLeapYear(2023)


# 9. Write a program that asks the user to enter a number and prints out all the divisors of that
# number. [Hint: the % operator is used to tell if a number is divisible by something.]

def printDivisors(root:int):
    divisors = []
    for i in range(1, int((root/2)+1)):
        if root%i==0:
            divisors.append(i)
        else:
            pass
    print(divisors)
# printDivisors(400)


# 10. Write a multiplication game program for kids. The program should give the player ten randomly 
# generated multiplication questions to do. After each, the program should tell them
# whether they got it right or wrong and what the correct answer is.
# Question 1: 3 x 4 = 12
# Right!
# Question 2: 8 x 6 = 44
# Wrong. The answer is 48.
# ...
# ...
# Question 10: 7 x 7 = 49
# Right.

def questionGame():
    score = 0
    for i in range(1,11):
        a = randint(1, 20)
        b = randint(1, 20)
        answer = eval(input('Question ' + str(i) + ': ' + str(a) + ' * ' + str(b) + ' = '))
        if answer == a*b:
            print('Right')
            print('Question ' + str(i) + ': ' + str(a) + ' * ' + str(b) + ' = ' + str(a*b))
            score+=1
        else:
            print('Wrong')
            print('Question ' + str(i) + ': ' + str(a) + ' * ' + str(b) + ' = ' + str(a*b))
    print('Your score is', score)
# questionGame()


# 11. Write a program that asks the user for an hour between 1 and 12, asks them to enter am or pm,
# and asks them how many hours into the future they want to go. Print out what the hour will
# be that many hours into the future, printing am or pm as appropriate. An example is shown
# below.
# Enter hour: 8
# am (1) or pm (2)? 1
# How many hours ahead? 5
# New hour: 1 pm

def calcHoursAhead():
    initHour:int = eval(input('Enter hour: '))
    dayNight:int = eval(input('Enter 1 (AM) or 2 (PM): '))
    hoursAhead:int = eval(input('How many hours ahead?: '))
    
    gmt = ['AM', 'PM']
    total = initHour + hoursAhead
    check12 = total%12
    check24 = total%24
    check24_12 = check24%12
    time = 0
    if total < 12:
        time = total
        print('New Hour: ' + str(time) + gmt[dayNight-1])
    elif total == 12:
        time = 12
        if dayNight == 1:
            print('New Hour: ' + str(time) + gmt[dayNight])
        elif dayNight == 2:
            print('New Hour: ' + str(time) + gmt[dayNight-1])
    elif total<24 and total>12:
        time = check12
        if dayNight == 1:
            print('New Hour: ' + str(time) + gmt[dayNight])
        elif dayNight == 2:
            print('New Hour: ' + str(time) + gmt[dayNight-1])
    elif total == 24:
        time = 12
        print('New Hour: ' + str(time) + gmt[dayNight-1])
    elif total>24:
        if check24>12:
            time = check24_12
            if dayNight == 1:
                print('New Hour: ' + str(time) + gmt[dayNight])
            elif dayNight == 2:
                print('New Hour: ' + str(time) + gmt[dayNight-1])
        else:
            time = check24
            print('New Hour: ' + str(time) + gmt[dayNight-1])

# calcHoursAhead()
            


# 12. A jar of Halloween candy contains an unknown amount of candy and if you can guess exactly
# how much candy is in the bowl, then you win all the candy. You ask the person in charge the
# following: If the candy is divided evenly among 5 people, how many pieces would be left
# over? The answer is 2 pieces. You then ask about dividing the candy evenly among 6 people,
# and the amount left over is 3 pieces. Finally, you ask about dividing the candy evenly among
# 7 people, and the amount left over is 2 pieces. By looking at the bowl, you can tell that there
# are less than 200 pieces. Write a program to determine how many pieces are in the bowl.

def calcCandy():
    for i in range(1, 200):
        if i%5==2 and i%6==3 and i%7==2:
            print(i)
# calcCandy()


# 13. Write a program that lets the user play Rock-Paper-Scissors against the computer. There
# should be five rounds, and after those five rounds, your program should print out who won
# and lost or that there is a tie.

def rockpaperScissors():
    playerName = input('Enter your alias: ')
    playerScore = 0
    computerScore = 0
    raffle = {1:'Rock', 2:'Paper', 3:'Scissors'}
    for i in range(5):
        computerDraw = raffle[randint(1,3)]
        playerDraw:int = raffle[eval(input('Enter 1(Rock), 2(Paper) or 3(Scissors): '))]
        if computerDraw == playerDraw:
            pass
        elif computerDraw==raffle[1] and playerDraw==raffle[2]:
            playerScore+=1
        elif computerDraw==raffle[1] and playerDraw==raffle[3]:
            computerScore+=1
        elif computerDraw==raffle[2] and playerDraw==raffle[1]:
            computerScore+=1
        elif computerDraw==raffle[2] and playerDraw==raffle[3]:
            playerScore+=1
        elif computerDraw==raffle[3] and playerDraw==raffle[1]:
            playerScore+=1
        elif computerDraw==raffle[3] and playerDraw==raffle[2]:
            computerScore+=1
        print('\n')
        print('Computer', computerDraw, ':', playerDraw, playerName)
        print('Computer', computerScore, ':', playerScore, playerName, '\n')
        
    if computerScore>playerScore:
        print('Computer', computerScore, ':', playerScore, playerName)
        print('Too Bad, You Failed\n')
    elif playerScore>computerScore:
        print('Computer', computerScore, ':', playerScore, playerName)
        print('Congrats, You Won\n')
    elif playerScore==computerScore:
        print('Computer', computerScore, ':', playerScore, playerName)
        print('It\'s A Tie\n')
# rockpaperScissors()