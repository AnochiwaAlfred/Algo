
# 19. Write a program that repeatedly asks the user to enter a birthday in the format month/day
# (like 12/25 or 2/14). The user indicates they are done entering birthdays by entering done.
# The program should return a count of how many of those birthdays are in February and how
# many are on the 25th of some month (any month).


class BirthMonth:
    def dateIn():
        date = input('Enter BirthDay in the format DD/MM e.g. 24/09 \n-->')
        return date
    def dateChkLen():    
        dt = dateIn()
        if len(dt) != 5 or '/' not in dt or int(dt[-2] + dt[-1]) > 12 or int(dt[0] + dt[1]) > 31:
            print('Incorrect Birthday Format')
            dateChkLen()
        else:
            return dt
    def dater():
        ddi = {}
        try:
            i = int(input('Enter the Number of Birthdays to Input: ')) 
        except Exception as e:
            print(e + '/n Enter an integer')
        for j in range(0, i):
            dt2 = str(dateChkLen())
            key = dt2[0] + dt2[1]
            value = int(dt2[-2] + dt2[-1])
            ddi.update({key:value})
        return ddi
    def datre():
        dd = dater()
        dddk = []
        dddv = []
        ddk = dd.keys()
        ddv = dd.values()
        for i in ddk:
            dddk.append(i)
        for j in ddv:
            dddv.append(j)
        a = str(dddk.count('25'))
        b = str(dddv.count(2))
        print('There are ' + b + ' birthdays in the month of February')
        print('There are ' + a + ' people born on the 25th')
    datre()
    