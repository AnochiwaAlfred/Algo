# 1. Write a function called rectangle that takes two integers m and n as arguments and prints
# out an m × n box consisting of asterisks. Shown below is the output of rectangle(2,4)
# ****
# ****

def rectangle(m,n):
    for i in range(m):
        print('*'*n)
# rectangle(5,15)

# 3. Write a function called sum_digits that is given an integer num and returns the sum of the
# digits of num.

def sum_digits(num):
    list1 = [int(i) for i in str(num)]
    sum = 0
    for i in list1:
        sum = sum + i
    print(sum)
# sum_digits(456)


# 7. Write a function that takes an integer n and returns a random integer with exactly n digits. For
# instance, if n is 3, then 125 and 593 would be valid return values, but 093 would not because
# that is really 93, which is a two-digit number.
from random import randint, random
def inter(n):
    def ran():
        num = randint(1,9999)
        if len(str(num)) != len(str(n)):
            ran()
        print(num)
    ran()
# inter(245)
    
# 8. Write a function called number_of_factors that takes an integer and returns how many
# factors the number has.


def number_of_factors(n):
    f = []
    for i in range(1, (n-1)):
        if n%i == 0:
            f.append(i)
        else:
            pass
    print(len(f))
# number_of_factors(100)

# 9. Write a function called factors that takes an integer and returns a list of its factors.


def factors(n):
    f = []
    for i in range(1, (n-1)):
        if n%i == 0:
            f.append(i)
        else:
            pass
    print(f)
# factors(100)


# 13. Write a function called change_case that given a string, returns a string with each upper
# case letter replaced by a lower case letter and vice-versa.

def change_case(sentence):
    for i in sentence:
        if str(i).isupper() == True:
          sentence = sentence[:sentence.index(str(i))] + str(i).lower() + sentence[sentence.index(str(i)) + 1:]
        else:
            pass
        if str(i).islower() == True:
              sentence = sentence[:sentence.index(str(i))] + str(i).upper() + sentence[sentence.index(str(i)) + 1:]
        else:
            pass
    print(sentence)
# change_case('AlfredM')

# 15. Write a function called root that is given a number x and an integer n and returns x ^ 1/n.
# In the function definition, set the default value of n to 2.

def root(x,n=2):
    return x ** (1/n)
# print(root(3,6))
