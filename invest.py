# 1. Write a class called Investment with fields called principal and interest. The construc￾tor should set the values of those fields. 
# There should be a method called value_after that
# returns the value of the investment after n years. The formula for this is p(1 + i)n
# , where p is
# the principal, and i is the interest rate. It should also use the special method __str__ so that
# printing the object will result in something like below:
# Principal - $1000.00, Interest rate - 5.12%


class Investment:
    def __init__(self, p, i):
        self.p = p
        self.i = i
    
  
    def value_after(self, n):
        return self.p * (1 + self.i) * n
    
    def __str__(self):
        n = eval(input('Enter the number of years: '))
        return  'With Principal - $' + str(self.p) + ', Interest Rate - ' + str(self.i) + '%. ' + 'The Value after ' + str(n) + ' years is $' + str(self.value_after(n))
    

a = Investment(100000, 7)
b = Investment(15000, 20)
c = Investment(1000, 5.12)
d = Investment(5000, 1)


print(a.__str__())
print(b.__str__())
print(c.__str__())
print(d.__str__())