
from string import ascii_lowercase

# 1. Write a program that uses list and range to create the list [3,6, 9, . . . , 99].

def ex1():
    l = list(range(3,100,3))
    print(l)


# 3. Write a program that asks the user to enter a word. Rearrange all the letters of the word
# in alphabetical order and print out the resulting word. For example, abracadabra should
# become aaaaabbcdrr.

def sortWords():
    l = []
    word = input('Enter a word: ')
    for i in ascii_lowercase:
        for j in word:
            if i == j:
                l.append(j)
    s = ''.join(l)
    print(s)

# 4. Write a program that takes a list of ten prices and ten products, applies an 11% discount to
# each of the prices displays the output like below, right-justified and nicely formatted.
# Apples $ 2.45
# Oranges $ 18.02
# ...
# Pears $120.03

def ex4():
    items = ['Kiwi', 'Peach', 'Strawberry', 'Watermelon', 'Cucumber', 'Banana', 'Mango', 'Pineapple', 'Orange', 'Apple']
    price = [23, 18, 24, 13, 35, 19, 31, 30, 16, 21]
    for i in price:
        price[price.index(i)] = i - (i * 0.11)
    for i in range(0, 10):
        print('{:>10s}'.format(items[i]) + '{:>6s}'.format(' $' + str('{:.2f}'.format(price[i]))))


# 5. Use the following two lists and the format method to create a list of card names in the format
# card value of suit name (for example, 'Two of Clubs').
# suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
# values = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
# 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']

def ex5():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
    'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
    cardValue = [a + ' of ' + b for b in suits for a in values]
    for i in cardValue:
        print(i)

# 6. Write a program that uses a boolean flag variable in determining whether two lists have any
# items in common.

def ex6():
    list1 = list(input('Enter a string of text: '))
    list2 = list(input('Enter another string of text: '))
    flag = False
    for i in list1:
        if i in list2:
            flag = True
    print(flag)
# ex6()



# 7. Write a program that creates the list [1,11,111,1111,...,111...1], where the entries
# have an ever increasing number of ones, with the last entry having 100 ones.

def ex7():
    list1 = [int('1'*i) for i in range(1, 101)]
    print(list1)
# ex7()
# 8. Write a program to find all numbers between 1 and 1000 that are divisible by 7 and end in a
# 6.

def ex8():
    l = [i for i in range(1000) if i%7==0 and str(i)[-1]=='6']
    print(l)

# 9. Write a program to determine how many of the numbers between 1 and 10000 contain the
# digit 3.

def ex9():
    l = [i for i in range(10000) if '3' in str(i)]
    print(len(l))

# 10. Adding certain numbers to their reversals sometimes produces a palindromic number. For
# instance, 241 + 142 = 383. Sometimes, we have to repeat the process. For instance, 84 + 48 =
# 132 and 132 + 231 = 363. Write a program that finds both two-digit numbers for which this
# process must be repeated more than 20 times to obtain a palindromic number.

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def add_to_reverse(num):
    return num + int(str(num)[::-1])

numbers = []
for num in range(10, 100):
    count = 0
    n = num
    while not is_palindrome(n):
        n = add_to_reverse(n)
        count += 1
        if count > 20:
            numbers.append(num)
            break

print(numbers)


# 11. Write a program that finds all pairs of six-digit palindromic numbers that are less than 20
# apart. One such pair is 199991 and 200002.

def is_palindrome(num):
    return str(num) == str(num)[::-1]

palindrome_pairs = []
for num1 in range(100000, 1000000):
    if not is_palindrome(num1):
        continue
    for num2 in range(num1 + 1, num1 + 20):
        if is_palindrome(num2):
            palindrome_pairs.append((num1, num2))

print(palindrome_pairs)


# 12. The number 1961 reads the same upside-down as right-side up. Print out all the numbers
# between 1 and 100000 that read the same upside-down as right-side up.

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def is_palindrome_number(num):
    num_str = str(num)
    upside_down_str = ""
    for digit in num_str:
        if digit == "0":
            upside_down_str += "0"
        elif digit == "1":
            upside_down_str += "1"
        elif digit == "6":
            upside_down_str += "9"
        elif digit == "8":
            upside_down_str += "8"
        elif digit == "9":
            upside_down_str += "6"
        else:
            return False
    return upside_down_str == num_str

palindrome_numbers = []
for num in range(1, 100001):
    if is_palindrome(num) and is_palindrome_number(num):
        palindrome_numbers.append(num)

print(palindrome_numbers)


# 13. The number 99 has the property that if we multiply its digits together and then add the sum
# of its digits to that, we get back to 99. That is, (9 × 9) + (9 + 9) = 99. Write a program to find
# all of the numbers less than 10000 with this property. (There are only nine of them.)

def ex13():
    for i in range(19, 10001):
        j = str(i)
        prod = 1
        sum = 0
        for a in j:
            prod *= int(a)
            sum += int(a)
        if prod + sum == i:
            print(i)

# 14. Write a program to find the smallest positive integer that satisfies the following property: If
# you take the leftmost digit and move it all the way to the right, the number thus obtained is
# exactly 3.5 times larger than the original number. For instance, if we start with 2958 and move
# the 2 all the way to the right, we get 9582, which is roughly 3.2 times the original number.

def ex14():
    flag = False
    i = 10
    while flag == False:
        v = float(str(i)[1:(len(str(i)))] + str(i)[0])
        if v == 3.2*i:
            flag == True
            print(i,v)
        i+=1
ex14()



# 15. Write a program to determine how many zeroes 1000! ends with.
import math
def ex15():
    fac = str(math.factorial(1000))
    count = 0
    # for i in fac:
    #     if i == '0':
    #         count+=1
    # print(count)
    for i in fac[::-1]:
        if i == '0':
            count+=1
        else:
            break
    print(count)
# ex15()

# 16. Write a program that converts a decimal height in feet into feet and inches. For instance, an
# input of 4.75 feet should become 4 feet, 9 inches.

def ex16():
    feet = eval(input('Enter a height in feet'))

# 20. Write a program that asks the user to enter a date in the format mm/dd/yy and converts it
# to a more verbose format. For example, 02/04/77 should get converted into February 4,
# 1977.

def changeDateFormat():
    dateIn = input('Enter  a date in the format mm/dd/yyyy')
    
