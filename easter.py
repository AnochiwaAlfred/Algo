# Easter is either March (22+d +e) or April (d +e−9). There is an exception if d = 29 and e = 6.
# In this case, Easter falls one week earlier on April 19. There is another exception if d = 28,
# e = 6, and m = 2, 5, 10, 13, 16, 21, 24, or 39. In this case, Easter falls one week earlier on April
# 18. Write a program that asks the user to enter a year and prints out the date of Easter in that
# year.


class EasterD:
    
    def easter():
        dater = None
        Y = eval(input('Enter a year: '))
        C = eval(str(Y)[0] + str(Y)[1])
        m = (15 + C - (C // 4) - (((8*C) + 13)//25)) % 30
        n = (4 + C - (C // 4)) % 7
        a = Y % 4
        b = Y % 7
        c = Y % 19
        d = ((19*c) + m) % 30
        e = ((2*a) + (4*b) + (6*d) + n) % 7
        if d == 29 and e == 6:
            dater = 'April 19'
        if d == 28 and e == 6 and m == (2 or 5 or 10 or 13 or 16 or 21 or 24 or 39):
            dater = 'April 18'
        else:
            mr = 22 + d + e
            ap = d + e - 9
            if mr <= 31:
                dater = 'March ' +  str(mr)
            else:
                dater = 'April ' +  str(ap)
        today = date.today().year
        if today > Y:
            Easter = 'Easter was ' +  str(dater)
        if today == Y:
            Easter = 'Easter is ' +  str(dater)
        if today < Y:
            Easter = 'Easter will be ' +  str(dater) 
        print(Easter)
    # easter()