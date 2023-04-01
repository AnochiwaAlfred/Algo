from random import choice

# 1. The code below prints the numbers from 1 to 50. Rewrite the code using a while loop to
# accomplish the same thing.
# for i in range(1,51):
#   print(i)

def ex1():
    i = 1
    while i < 51:
        print(i)
        i+=1


# 2. (a) Write a program that uses a while loop (not a for loop) to read through a string and print
# the characters of the string one-by-one on separate lines.
def ex2():
    string = 'Alfred'
    i = 0
    while i < len(string):
        print(string[i])
        i+=1

# (b) Modify the program above to print out every second character of the string.


# 14. Write a program to play the following simple game. The player starts with $100. On each
# turn a coin is flipped and the player has to guess heads or tails. The player wins $9 for each
# correct guess and loses $10 for each incorrect guess. The game ends either when the player
# runs out of money or gets to $200.

def moneyGame():
    cash = 100
    print('You start with $100. \n Every correct choice adds $9.')
    print('Every incorrect choice subtracts $10. To quit type \'quit\' ')
    while 0 < cash < 200:
        choices = ['heads', 'tails']
        program = choice(choices)
        if program == choices[0]:
            program2 = choices[1]
        if program == choices[1]:
            program2 = choices[0]
        player = input('heads or tails: ')
        if player in program:
            cash += 9
            print('You guessed correctly')
            print('You have $' + str(cash) + ' now.')
        if player in program2:
            cash -= 10
            print('You chose poorly')
            print('You have $' + str(cash) + ' now.')
        if player in 'quit':
            break
        print(program, program2)



# 15. Write a program to play the following game. There is a list of several country names and the
# program randomly picks one. The player then has to guess letters in the word one at a time.
# Before each guess the country name is displayed with correctly guessed letters filled in and
# the rest of the letters represented with dashes. For instance, if the country is Canada and the
# player has correctly guessed a, d, and n, the program would display -ana-da. The program
# should continue until the player either guesses all of the letters of the word or gets five letters australia, africa, nroth america, south america, asia, antartic, europe
# wrong.
"""
def listCountries():
    countries = ['USA', 'Nigeria', 'Spain', 'Canada', 'England', 'Italy', 'France', 'Australia', 'India',
                 'China', 'Japan', 'Brazil', 'Korea', 'Russia', 'Kenya', 'Ghana', 'Senegal', 'Jamaica', 
                 'Mexico', 'Syria', 'Egypt', 'Turkey', 'Greece', 'Germany']
    failCount = 0
    
    program = choice(countries).lower()
    placeholder = '_ '*len(program)
    print('The program has chosen a country.\n It has ' + str(len(program)) + 
          ' letters. \n Guess the country right with the letters. ')
    
    while placeholder != program or failCount < 5:
        print(placeholder)
        player = input('Enter a correct letter in the Country Name \n --> ')
        if player in program:
            pos = program.find(player)
            # remove the space between the characters
            for i in range(placeholder.count(' ')):
                placeholder = placeholder.replace(' ', '')
            # replace the dash with the value
            placeholder  = placeholder[:pos] + player + placeholder[pos+1:]
            # convert to list
            placeholder2 = list(placeholder)
            # insert the space between characters
            for i in range(1, len(placeholder2) + len(placeholder2) - 1, 2):
                placeholder2.insert(i, ' ')
            # convert back to string
            placeholder = ''.join(placeholder2)
        if player not in program:
            failCount += 1
    if placeholder == program:
        print('Congratulations, You guessed the country correctly!!!')
        print(program.title())
    if failCount == 5:
        print('Sorry, you guessed wrong. The country is ' + program.title())
listCountries() 
"""

