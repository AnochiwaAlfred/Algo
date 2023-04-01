
# 15. Write a program to play the following game. There is a list of several country names and the
# program randomly picks one. The player then has to guess letters in the word one at a time.
# Before each guess the country name is displayed with correctly guessed letters filled in and
# the rest of the letters represented with dashes. For instance, if the country is Canada and the
# player has correctly guessed a, d, and n, the program would display -ana-da. The program
# should continue until the player either guesses all of the letters of the word or gets five letters australia, africa, nroth america, south america, asia, antartic, europe
# wrong.

from random import choice

class GuessCountry:
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
            player = (input('Enter a correct letter in the Country Name \n --> ')).lower()
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
    # listCountries() 

g = GuessCountry()
g.listCountries()