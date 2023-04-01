class Dater():
    def date():
        inp = input(' This is a 19th century calendar. \n Enter a date in the format dd/mm/yy: ')
        try:
            dd = int(inp[0] + inp[1])
        except Exception as e:
            print(str(e) + '\n Enter date DIGITS!!!')
        try:
            mm = int(inp[3] + inp[4])
        except Exception as e:
            print(str(e) + '\n Enter date DIGITS!!!')
        try:
            yy = int(inp[6] + inp[7])
        except Exception as e:
            print(str(e) + '\n Enter date DIGITS!!!')
        f1 = len(inp) == 8
        f2 = mm <= 12
        if mm == (1 or 3 or 5 or 7 or 8 or 10 or 12):
            a = 31
            f3 = dd == a
        elif mm == (4 or 6 or 9 or 11):
            a = 30
            f3 = dd == a
        else:
            a = 29
            f3 = dd == (28 or 29)
                
        # dd = int(input('Enter date(dd) '))
        # mm = int(input('Enter date(mm) '))
        # yy = input('Enter date(yyyy) ')
        # print('The date is ' + str(dd) + '-' + str(mm) + '-' + yy)
        months = ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

        mm2 = months[mm]

        # if f1 and f2 and f3 == True:
        #     print('The date is ' + mm2 + ' ' + str(dd) + ', ' + '19' + str(yy))
        # else:
        #     print(mm2 + ' has only ' + a + ' days!!!')
        print('The date is ' + mm2 + ' ' + str(dd) + ', ' + '19' + str(yy))
    date()
