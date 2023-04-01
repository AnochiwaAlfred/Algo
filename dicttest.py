
# 1. Write a program that repeatedly asks the user to enter product names and prices. Store all
# of these in a dictionary whose keys are the product names and whose values are the prices.
# When the user is done entering products and prices, allow them to repeatedly enter a product
# name and print the corresponding price or a message if the product is not in the dictionary.

def productlist():
    productlists = {}
    item = ''
    while item != 'STOP':
        item = input('Enter Product Name. To stop enter STOP: ')
        if item == 'STOP':
            break
        price = int(input('Enter Product Price: '))
        productlists[item] = price
    print('To get a product price, type the name of the product')
    while item != 'STOP':
        item = input('Enter Product Name. To stop enter STOP: ')
        print(item, productlists[item])
        return productlists
    print(productlist)
# productlist()

# 3. For this problem, use the dictionary from the beginning of this chapter whose keys are month
# names and whose values are the number of days in the corresponding months.
# (a) Ask the user to enter a month name and use the dictionary to tell them how many days
# are in the month.
# (b) Print out all of the keys in alphabetical order.
# (c) Print out all of the months with 31 days.
# (d) Print out the (key-value) pairs sorted by the number of days in each month
# (e) Modify the program from part (a) and the dictionary so that the user does not have to
# know how to spell the month name exactly. That is, all they have to do is spell the first
# three letters of the month name correctly.

def monthsdays():
    days = {
            'January':31, 'February':28, 'March':31, 'April':30,
            'May':31, 'June':30, 'July':31, 'August':31,
            'September':30, 'October':31, 'November':30, 'December':31
        }
    month = input('Enter a month name e.g February: ')
    print('There are', days[month], 'days in', month )
    days2 = list(days.keys())
    days2.sort()
    print(days2)
    for i in days:
        if days[i] == 31:
            print(i)
    # days3 = list(days.values())
    # days3.sort()
    # for i in days3:
    #   print(days.get(i), i)
# monthsdays()

# 4. Write a program that uses a dictionary that contains ten user names and passwords. The
# program should ask the user to enter their username and password. If the username is not in
# the dictionary, the program should indicate that the person is not a valid user of the system. If
# the username is in the dictionary, but the user does not enter the right password, the program
# should say that the password is invalid. If the password is correct, then the program should
# tell the user that they are now logged in to the system.

def login_sys():
    login_deets = {'anochiwaalfred':'Alfieolli2409', 'anochiwadavid':'surreal', 
                   'cryptalz':'Alfieolli', 'obiankechuks':'191919',
                   'angelzubby1':'gold', 'anointedngeorge':'odoo', 'aarequiem':'netflixandchill', 
                   'stellilogreen':'tristan42', 'lanochiwa':'alfred.123#',
                   'anochiwar':'197070', 'ralphcompton':'fastdraw23'}
    def login():
        a = input('Enter your Username:  ')
        if a in login_deets.keys():
            def password():
                b = input('Enter Password: ')
                if b == login_deets[a]:
                    print('You are now logged into the system')
                else:
                    print('Password Incorrect!!!')
                    password()
            password()
        else:
            print('User does not exist')
            login()
    login()
# login_sys()


# 12. Below are the notes used in music:
# C C# D D# E F F# G G# A A# B
# The notes for the C major chord are C, E, G. A mathematical way to get this is that E is 4 steps
# past C and G is 7 steps past C. This works for any base. For example, the notes for D major
# are D, F#, A. We can represent the major chord steps as a list with two elements: [4,7]. The
# corresponding lists for some other chord types are shown below:
# Minor [3,7]               Dominant seventh [4,7,10]
# Augmented fifth [4,8]     Minor seventh [3,7,10]
# Minor fifth [4,6]         Major seventh [4,7,11]
# Major sixth [4,7,9]       Diminished seventh [3,6,10]
# Minor sixth [3,7,9]
# Write a program that asks the user for the key and the chord type and prints out the notes of
# the chord. Use a dictionary whose keys are the (musical) keys and whose values are the lists
# of steps.


def chords():
    type = {'Major':[4,7], 'Minor':[3,7], 'Diminished':[3,6],
            'Augmented':[4,8], 'Minor Sixth':[3,7,9], 'Major Sixth':[4,7,9],  
            'Dominant Seventh':[4,7,10], 'Minor Seventh':[3,7,10], 'Major Seventh':[4,7,11], 
            'Minor Major Seventh':[3,7,11], 'Diminished Seventh':[3,6,10], 'Ninth':[4,7,11,2]}
    keys = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#','A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
    print('\nCHORD TYPES')
    for i in type.keys():
        print(i)
    print('N/B: Capitalize Each Word!!!!')
    key = str(input('\nEnter Key: ')).title()
    ty = str(input('Enter chord type: ')).title()
    chord = [key]
    for i in type[ty]:
        chord.append(keys[keys.index(key)+i])
    print('The notes of ' + key + ' ' + ty + ' are ' + '-'.join(chord))
# chords()


# 14. Dictionaries provide a convenient way to store structured data. Here is an example dictionary:
# d=[{'name':'Todd', 'phone':'555-1414', 'email':'todd@mail.net'},
# {'name':'Helga', 'phone':'555-1618', 'email':'helga@mail.net'},
# {'name':'Princess', 'phone':'555-3141', 'email':''},
# {'name':'LJ', 'phone':'555-2718', 'email':'lj@mail.net'}]
# Write a program that reads through any dictionary like this and prints the following:
# (a) All the users whose phone number ends in an 8
# (b) All the users that don’t have an email address listed


def studentData():
    data=[
        {'username':'anochiwaalfred', 'password':'Alfieolli2409', 'firstname':'Alfred', 'lastname':'Anochiwa',
             'gender':'Male', 'phone':'08166646601', 'email':'anochiwaalfred@gmail.com'},
        {'username':'anochiwadavid', 'password':'surreal', 'firstname':'David', 'lastname':'Anochiwa',
             'gender':'Male', 'phone':'07043663277', 'email':'anochiwadavid@gmail.com'},
        {'username':'cryptalz', 'password':'Alfieolli', 'firstname':'Cryptalz', 'lastname':'Zirconium',
             'gender':'Male', 'phone':'09027274550', 'email':'cryptalz@gmail.com'},
        {'username':'obiankechuks', 'password':'191919', 'firstname':'Othniel', 'lastname':'Obianke',
             'gender':'Male', 'phone':'08157235108', 'email':'obiankechuks@gmail.com'},
        {'username':'angelzubby1', 'password':'GOLD', 'firstname':'Esther', 'lastname':'John',
             'gender':'Female', 'phone':'09133932759', 'email':'angelzubby1@gmail.com'},
        {'username':'anointedngeorge', 'password':'odoo', 'firstname':'George', 'lastname':'Onovo',
             'gender':'Male', 'phone':'07045072930', 'email':'anointedngeorge@gmail.com'},
        {'username':'aarequiem', 'password':'neflixandchill', 'firstname':'Klaus', 'lastname':'Mikaelson',
             'gender':'Male', 'phone':'07068393274', 'email':'aarequiem@yahoo.com'},
        {'username':'stellilogreen', 'password':'tristan42', 'firstname':'Stella', 'lastname':'Brown',
             'gender':'Female', 'phone':'08106615364', 'email':'stellilogreen@yahoo.com'},
        {'username':'lanochiwa', 'password':'alfred.123#', 'firstname':'Lasbrey', 'lastname':'Anochiwa',
             'gender':'Male', 'phone':'08033343850', 'email':'lanochiwa@gmail.com'},
        {'username':'anochiwar', 'password':'197070', 'firstname':'Roseline', 'lastname':'West',
             'gender':'Female', 'phone':'08156697322', 'email':'anochiwar@yahoo.com'},
        {'username':'ralphcompton', 'password':'fastdraw23', 'firstname':'Ralph', 'lastname':'Compton',
             'gender':'Male', 'phone':'08100908614', 'email':'ralphcompton@rocketmail.com'}
    ]
    

    for i in data:
        if i['email'] == '':
            print(i['firstname'], i['lastname'], ' has no email address.')
        if 'anochiwa' in i['email']:
            print(i['firstname'], i['lastname'])
studentData()

