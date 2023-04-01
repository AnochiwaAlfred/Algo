import string
from random import randint
vowels = ['a', 'e', 'i', 'o', 'u']


# 1. Write a program that asks the user to enter a string. The program should then print the
# following:
# (a) The total number of characters in the string
# (b) The string repeated 10 times
# (c) The first character of the string (remember that string indices start at 0)
# (d) The first three characters of the string
# (e) The last three characters of the string
# (f) The string backwards
# (g) The seventh character of the string if the string is long enough and a message otherwise
# (h) The string with its first and last characters removed
# (i) The string in all caps
# (j) The string with every a replaced with an e
# (k) The string with every letter replaced by a space

def stringEx1():
    string = input('Enter a string: ')
    print(len(string))
    print(string*10)
    print(string[0])
    print(string[:3])
    print(string[-3:])
    print(string[ : : -1])
    print(string[6] if len(string)>=7 else 'Not long enough')
    print(string[1:-2])
    print(string.upper())
    newString = ''
    for i in string:
        if i!='a':
            newString=newString[:len(newString)]+i
        elif i=='a':
            newString=newString[:len(newString)]+'e'
    print(newString)
    newString2 = ''
    for i in string:
        if i.isalpha()==False:
            newString2=newString2[:len(newString2)]+i
        elif i.isalpha()==True:
            newString2=newString2[:len(newString2)]+' '
    print(newString2)
# stringEx1()
            
    

# 2. A simple way to estimate the number of words in a string is to count the number of spaces
# in the string. Write a program that asks the user for a string and returns an estimate of how
# many words are in the string.

def countWords():
    string = input('Enter a String: ')
    count = 0
    for i in string:
        if i==' ':
            count+=1
    print('Number of words:', count+1)
# countWords()


# 3. People often forget closing parentheses when entering formulas. Write a program that asks
# the user to enter a formula and prints out whether the formula has the same number of open-
# ing and closing parentheses.


# 4. Write a program that asks the user to enter a word and prints out whether that word contains
# any vowels.

def checkVowels(word):
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for letter in word:
        if letter in vowels:
            count+=1
    print('Number of vowels:', count)
    
# checkVowels('Papparazi')

# 5. Write a program that asks the user to enter a string. The program should create a new string
# called new_string from the user’s string such that the second character is changed to an
# asterisk and three exclamation points are attached to the end of the string. Finally, print
# new_string. Typical output is shown below:
# Enter your string: Qbert
# Q*ert!!!

def stringEx5(text):
    print(text[:1]+'*'+text[2:]+'!!!')
# stringEx5('Alfred')

# 6. Write a program that asks the user to enter a string s and then converts s to lowercase, re-
# moves all the periods and commas from s, and prints the resulting string.

def filterString(s):
    s = s.lower()
    for i in s:
        if i == '.' or i == ',':
            s=s.replace(i, '')
    print(s)
# filterString('We are genesys, arent we..')

# 7. Write a program that asks the user to enter a word and determines whether the word is a
# palindrome or not. A palindrome is a word that reads the same backwards as forwards.

def checkPalindrome(word):
    if word.lower() == word.lower()[ : :-1]:
        print('A Palindrome')
    else:
        print('Not A Palindrome')
# checkPalindrome('omo')
# checkPalindrome('omor')


# 9. Ask the user for a number and then print the following, where the pattern ends at the number
# that the user enters.
# 1
#  2
#   3
#    4

def stringEx9():
    n = eval(input('Enter a number: '))
    for i in range(1, n+1):
        print(' '*i + str(i))
# stringEx9()

# 10. Write a program that asks the user to enter a string, then prints out each letter of the string
# doubled and on a separate line. For instance, if the user entered HEY, the output would be
# HH
# EE
# YY

def stringEx10():
    word = input('Enter a String: ')
    for i in word:
        print(i*2)
# stringEx10()
    

# 12. Write a program that asks the user to enter a word and then capitalizes every other letter of
# that word. So if the user enters rhinoceros, the program should print rHiNoCeRoS.

def titlerX(word):
    word = word.lower()
    for i in range(1, len(word)+1):
        if i%2==0:
            word = word[:i-1]+word[i-1].upper()+word[i:]
    print(word)
# titlerX('Samicarter')


# 14. Write a program that asks the user to enter their name in lowercase and then capitalizes the
# first letter of each word of their name.

def titlerY(text):
    text = text.title()
    print(text)
# titlerY('anochiwa alfred')


# 17. Write a program that generates the 26-line block of letters partially shown below. Use a loop
# containing one or two print statements.
# abcdefghijklmnopqrstuvwxyz
# bcdefghijklmnopqrstuvwxyza
# cdefghijklmnopqrstuvwxyzab
# ...
# yzabcdefghijklmnopqrstuvwx
# zabcdefghijklmnopqrstuvwxy

def stringEx17():
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(alpha)):
        print(alpha[i:]+alpha[0:i])
# stringEx17()
    


# 19. Write a program that asks the user for a large integer and inserts commas into it according
# to the standard American convention for commas in large numbers. For instance, if the user
# enters 1000000, the output should be 1,000,000.

def punctuateNumber():
    num = input('Enter a number: ')
    num2=num[ : :-1]
    for i in range(2, ((len(num2))+(len(num2))//3), 4):
        num2 = num2[:i+1]+','+num2[i+1:]
    num=num2[ : :-1]
    if num[0]==',':
        num=num[1: ]
    print(num)
# punctuateNumber()


# 21. An anagram of a word is a word that is created by rearranging the letters of the original.
# For instance, two anagrams of idle are deli and lied. Finding anagrams that are real words is
# beyond our reach until Chapter 12. Instead, write a program that asks the user for a string
# and returns a random anagram of the string—in other words, a random rearrangement of the
# letters of that string.

def anagram():
    word = input('Enter a word: ')
    rand = []
    while len(rand)<len(word):
        num = randint(0,len(word)-1)
        if num not in rand:
            rand.append(num)
    newWord = ''
    for i in rand:
        newWord = newWord + word[i]
    print(newWord)
# anagram()


# 22. A simple way of encrypting a message is to rearrange its characters. One way to rearrange the
# characters is to pick out the characters at even indices, put them first in the encrypted string,
# and follow them by the odd characters. For example, the string message would be encrypted
# as msaeesg because the even characters are m, s, a, e (at indices 0, 2, 4, and 6) and the odd
# characters are e, s, g (at indices 1, 3, and 5).

# (a) Write a program that asks the user for a string and uses this method to encrypt the string.
# (b) Write a program that decrypts a string that was encrypted with this method.

def ex22():
    w = eval(input('enterlist'))
    print(type(w))
    print(w)


# 24. In calculus, the derivative of x^4 is 4x^3. The derivative of x^5 is 5x^4. The derivative of x^6 is 6x^5.
# This pattern continues. Write a program that asks the user for input like x^3 or x^25
# and prints the derivative. For example, if the user enters x^3, the program should print out
# 3x^2.

def derivative():
    dy = input('Enter a formular in the format x^3: ')
    cf = eval(dy[dy.index('^')+1:])
    derivative = str(cf) + 'x^' + str(cf-1)
    print(derivative) 

h = '_ _ _ _ _ _'

g = 'Alfred'
y = 'd'
# print(g)
pos = g.find(y)
for i in range(h.count(' ')):
    h = h.replace(' ', '')
h = h[:pos] + y + h[pos+1:]

print(h)
gl = list(h)
for i in range(1, len(gl) + len(gl) - 1, 2):
    gl.insert(i, ' ')
h = ''.join(gl)
print(h)
