from secrets import choice


# 14. Write a program to play the following simple game. The player starts with $100. On each
# turn a coin is flipped and the player has to guess heads or tails. The player wins $9 for each
# correct guess and loses $10 for each incorrect guess. The game ends either when the player
# runs out of money or gets to $200.


class Nairabet:
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
    moneyGame()