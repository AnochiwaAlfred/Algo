
# 4. Write a class called Time whose only field is a time in seconds. It should have a method called
# convert_to_minutes that returns a string of minutes and seconds formatted as in the fol￾lowing example:
#     if seconds is 230, the method should return '5:50'. It should also have
# a method called convert_to_hours that returns a string of hours, minutes, and seconds
# formatted analogously to the previous method.


class Time:
    
    def __init__(self, time):
        self.time = time
        
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    h = 0

    def convert_to_minutes(self):
        a = self.time // 60
        b = self.time % 60
        print(a, ' minutes and ', b, ' seconds.')
            
    def convert_to_hours(self):
        a = self.time // 3600
        b = self.time % 3600
        c = b // 60
        d = b % 60
        print(a, ' hours ', c, ' minutes ', d, ' seconds.')
    
    def convert_to_days(self):
        a = self.time // 86400
        b = self.time % 86400
        c = b // 3600
        d = b % 3600
        e = d // 60
        f = d % 60
        print(a, ' days ', c, ' hours', e, 'minutes ', f, ' seconds.')
        
    def convert_to_years(self):
        g = self.time // 31536000000 
        h = self.time % 31536000000
        if h<365:  
            a = h // 86400
            b = h % 86400
        else:
            pass
        c = b // 3600
        d = b % 3600
        e = d // 60
        f = d % 60
        print(g, ' years ', a, ' days ', c, ' hours', e, 'minutes ', f, ' seconds.')        
    
    def convert(self):
        # self.time = int(input('Enter a number of seconds: '))

        if self.time < 60:
            print(self.time, ' seconds')
            
        elif self.time < 3600:
            self.convert_to_minutes()
            
        elif self.time < 86400:
            self.convert_to_hours()
            
        elif self.time < 31536000000:
            self.convert_to_days()
            
        else:
            self.convert_to_years()
            
            
            
t = Time(400)
t.convert()