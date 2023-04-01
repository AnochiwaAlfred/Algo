from random import randint


# Write a program that lets the user play Rock-Paper-Scissors against the computer. There
# should be five rounds, and after those five rounds, your program should print out who won
# and lost or that there is a tie.


class RockPaperScissors:
    def rps():
        player = 0
        computer = 0
        for i in range(5):
            a = randint(1,3)
            def chk():
                inp = input('Enter your choice (Rock, Paper or Scissors): ')
                if 'ock' or 'roc' or 'Roc' in inp:
                    return 1
                if 'ape' or 'per' or 'Pap' or 'pap' in inp:
                    return 2
                if 'sci' or 'Sci' or 'sor' or 'cis' in inp:
                    return 3
                else:
                    chk()
            b = chk()
            if a == 1:
                if b == 1:
                    pass
                if b == 2:
                    player += 1
                if b == 3:
                    computer += 1
            if a == 2:
                if b == 1:
                    computer += 1
                if b == 2:
                    pass
                if b == 3:
                    player += 1   
            if a == 3:
                if b == 1:
                    player += 1
                if b == 2:
                    computer += 1
                if b == 3:
                    pass
            score = 'Computer ' + str(computer) + ':' + str(player) + ' Player'
            print('The score is ' +  score)
        if player == computer:
            print('Its a tie!!')
        if player > computer:
            print('You WON!!!!!!')
        if computer > player:
            print('You Lost!')
        else:
            pass
        again = input('Play Again? Reply Yes or No: ')
        if 'Y' or 'y' or 'e' or 's' in again:
            rps()
        if 'N' or 'n' or 'o' or 'O' in again:
            print(' ')
    rps()
