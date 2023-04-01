


class Password_manager2:
    def __init__(self, old_passwords):
        self.old_passwords = old_passwords 
        
    def get_password(self):
        current_password = ''
        current_password = self.old_passwords[(len(current_password) - 1)]
        return current_password
    
    def set_password(self):
        def new_pass_input():
            new_pass = input('Enter new password: ')
            new_pass2 = input('Enter password again: ')
            if new_pass == new_pass2:
                return new_pass
            else:
                print('Password mismatch!!!')
                new_pass_input()
        def set_pass():
            new_pass = new_pass_input()
            flag = False
            for i in self.old_passwords:
                if i == new_pass:
                    flag = True
                else:
                    pass
            if flag == False:
                # print(new_pass)
                self.old_passwords.append(new_pass)
            else:
                print('You\'ve entered an old password!!')
                set_pass()
            print('New Password set succesfully')
            return new_pass
        new_pass=set_pass()
        return new_pass
        



def login_sys():
    login_deets = {'anochiwaalfred':'Alfieolli2409', 'anochiwadavid':'surreal', 
                   'cryptalz':'Alfieolli', 'obiankechuks':'191919',
                   'angelzubby1':'GOLD', 'anointedngeorge':'odoo', 'aarequiem':'netflixandchill', 
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
                    change = input('Forgot Password? Change it.  Enter Y or N: ')
                    if change == 'Y' or 'y':
                        passW = list(login_deets[a])
                        c = Password_manager2(passW)
                        new_pass = c.set_password()
                        login_deets[a] = new_pass
                        password()
                    else:
                        password()
            password()
        else:
            print('User does not exist')
            login()
    login()

login_sys()



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
# studentData()
