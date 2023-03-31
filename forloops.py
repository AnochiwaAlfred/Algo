# 1. Write a program that prints your name 100 times.

def printNameHundredTimes(name):
   for i in range(101):
      print(name)
# printNameHundredTimes('Alfred')


# 3. Write a program that outputs 100 lines, numbered 1 to 100, each with your name on it. The
# output should look like the output below.
# 1 Your name
# 2 Your name
# 3 Your name
# 4 Your name
# ...
# 100 Your name

def printNameHundredTimesWithNumbering(name):
   for i in range(101):
      print(i, name)
# printNameHundredTimesWithNumbering('Alfred')

# 4. Write a program that prints out a list of the integers from 1 to 20 and their squares. The output
# should look like this:
# 1 --- 1
# 2 --- 4
# 3 --- 9
# ...
# 20 --- 400

def intSquare(n:int):
   for i in range(1, n+1):
      print(i, '---', i**2)
# intSquare(20)
   
   


# 5. Write a program that uses a for loop to print the numbers 8, 11, 14, 17, 20, . . . , 83, 86, 89.

def ex5():
   for i in range(8, 90, 3):
      print(i, end='\n')
# ex5()

# 6. Write a program that uses a for loop to print the numbers 100, 98, 96, . . . , 4, 2.

def ex6():
   for i in range(100, 0, -2):
      print(i, end='\n')
# ex6()

# 8. Write a program that asks the user for their name and how many times to print it. The program should print out the user’s name the specified number of times.

def printNameNTimes(name, n:int):
   for i in range(n):
      print(name, end='\n')
# printNameNTimes('Alfred', 30)

# 9. The Fibonacci numbers are the sequence below, where the first two numbers are 1, and each
# number thereafter is the sum of the two preceding numbers. Write a program that asks the
# user how many Fibonacci numbers to print and then prints that many.
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 . . .

def printFibonacciSequence(n:int):
   seq = [1,1]
   def addNewValue():
      length = len(seq)
      var = seq[length-1] + seq[length-2]
      seq.append(var)
      
   for i in range(n-2):
      addNewValue()
   print(seq)
# printFibonacciSequence(10)

