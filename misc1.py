import math

# 1. Write a program that counts how many of the squares of the numbers from 1 to 100 end in a 1.

def countSquares():
    count = 0
    for i in range(100):
        if str(i**2)[-1]=='1':
            count+=1
    print(count)
# countSquares()


# 2. Write a program that counts how many of the squares of the numbers from 1 to 100 end in a
#    4 and how many end in a 9.

def countSquares2():
    count4 = 0
    count9 = 0
    for i in range(101):
        if str(i**2)[-1]=='4':
            count4+=1
        elif str(i**2)[-1]=='9':
            count9+=1
    print(count4, 'ends in 4')
    print(count9, 'ends in 9')
# countSquares2()

# 3. Write a program that asks the user to enter a value n, and then computes 
#     (1 + 1/2 + 1/3 +...+1/n)-ln(n). The ln function is log in the math module.

def logFact(n:int):
    sum = 0
    for i in range(n+1):
        sum+=(1/n)
    print(sum)
    print(sum - math.log(n))
# logFact(20)
    
# 4. Write a program to compute the sum 1 − 2 + 3 − 4 + ··· + 1999 − 2000.

def alternateSums():
    sumE = 0
    sumO = 0
    for i in range(2001):
        if i%2==1:
            sumO+=i
        elif i%2==0:
            sumE+=i
    print(sumO-sumE)
# alternateSums()

# 5. Write a program that asks the user to enter a number and prints the sum of the divisors of
# that number. The sum of the divisors of a number is an important function in number theory.

def sumOfDivisors(n):
    sum = 0
    for i in range(1,int(n/2)+1):
        if n%i==0:
            sum+=i
        else:
            pass
    print(sum)
# sumOfDivisors(20)


# 6. A number is called a perfect number if it is equal to the sum of all of its divisors, not including
# the number itself. For instance, 6 is a perfect number because the divisors of 6 are 1, 2, 3, 6
# and 6 = 1 + 2 + 3. As another example, 28 is a perfect number because its divisors are 1, 2, 4,
# 7, 14, 28 and 28 = 1 + 2 + 4 + 7 + 14. However, 15 is not a perfect number because its divisors
# are 1, 3, 5, 15 and 15 6= 1 + 3 + 5. Write a program that finds all four of the perfect numbers
# that are less than 10000.


def perfectNumbers():
    pNum = []
    for n in range(1, 10001):
        sum = 0
        for i in range(1,int(n/2)+1):
            if n%i==0:
                sum+=i
            else:
                pass
        if sum==n:
            pNum.append(n)
    print(pNum)
# perfectNumbers()


# 7. An integer is called squarefree if it is not divisible by any perfect squares other than 1. For
# instance, 42 is squarefree because its divisors are 1, 2, 3, 6, 7, 21, and 42, and none of those
# numbers (except 1) is a perfect square. On the other hand, 45 is not squarefree because it is
# divisible by 9, which is a perfect square. Write a program that asks the user for an integer and
# tells them if it is squarefree or not.

def squareFree(n):
    divisor = []
    for i in range(1,int(n/2)+1):
        if n%i==0:
            check = True
            for k in range(1,int(i/2)+1):
                if k**2==i:
                    check&=False
            if check==False:
                divisor.append(i)
    if divisor==[]:
        print('SquareFree')
    else:
        print('Not SquareFree')
        print('Among its divisors is', divisor)
# squareFree(100)
    

# 8. Write a program that swaps the values of three variables x, y, and z, so that x gets the value
# of y, y gets the value of z, and z gets the value of x.

def swapper(x,y,z):
    print(x,y,z)
    x,y = y,x
    y,z = z,y
    print(x,y,z)
# swapper(2,3,4)

# 9. Write a program to count how many integers from 1 to 1000 are not perfect squares, perfect
# cubes, or perfect fifth powers.

def checkPerfection():
    imperfect = []
    perfect = []
    for i in range(1,1001):
        check = True
        for k in range(1,int(i/2)+1):
            if k**2==i:
                check&=False
            if k**3==i:
                check&=False
            if k**5==i:
                check&=False
        if check==True:
            imperfect.append(i)
        if check==False:
            perfect.append(i)
    # print(perfect)
    # print(imperfect)
    print(len(imperfect))
# checkPerfection()


# 10. Ask the user to enter 10 test scores. Write a program to do the following:
# (a) Print out the highest and lowest scores.
# (b) Print out the average of the scores.
# (c) Print out the second largest score.
# (d) If any of the scores is greater than 100, then after all the scores have been entered, print
# a message warning the user that a value over 100 has been entered.
# (e) Drop the two lowest scores and print out the average of the rest of them.

def ex10m():
    numbers = []
    for i in range(1,6):
        num:int=eval(input('Enter number '+str(i)+' : '))
        numbers.append(num)
    print(numbers)
    print(max(numbers), min(numbers))
    numbers.sort()
    print(numbers)
    print(numbers[-2])
    check100 = False
    for i in numbers:
        if i>100:
            check100|=True
    if check100==True:
        print('Error: A value over 100 has been entered')
    numbers.pop(0)
    numbers.pop(0)
    print(numbers)
# ex10m()

# 11. Write a program that computes the factorial of a number. The factorial, n!, of a number n is the
# product of all the integers between 1 and n, including n. For instance, 5! = 1 · 2 · 3 · 4 · 5 = 120.
# [Hint: Try using a multiplicative equivalent of the summing technique.]

def factorialX(n):
    product = 1
    for i in range(1, n+1):
        product*=i
    print(product)
# factorialX(6)


# 12. Write a program that asks the user to guess a random number between 1 and 10. If they guess
# right, they get 10 points added to their score, and they lose 1 point for an incorrect guess. Give
# the user five numbers to guess and print their score after all the guessing is done.

