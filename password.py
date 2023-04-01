
# 3. Write a class called Password_manager. The class should have a list called old_passwords
# that holds all of the user’s past passwords. The last item of the list is the user’s current password. 
# There should be a method called get_password that returns the current password
# and a method called set_password that sets the user’s password. The set_password
# method should only change the password if the attempted password is different from all
# the user’s past passwords. Finally, create a method called is_correct that receives a string
# and returns a boolean True or False depending on whether the string is equal to the current
# password or not.

class Password_manager:
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
        set_pass()
def run():
    passW = [
            'therealslim', 'netflixandchill',
            'AlfieXC', 'Alfieolli2409#', 'Alfieolli240999',
            'Alfieolli240999#', 'cryptalz1200', 'odoo', 'ij12345',
            'Alfieolli2409'
        ]
    c = Password_manager(passW)
    c.set_password()   
run()



