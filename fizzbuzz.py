

class FizzBuzz():
    
    def __init__(self, n):
        self.n = n

    def fizzBuzz(self):
        for i in range(1, self.n):
            if i % 15 == 0:
                print('FizzBuzz')
            elif i % 3 == 0:
                print('Fizz')
            elif i % 5 == 0:
                print('Buzz')
            else:
                print(i)

twi = FizzBuzz(200)
twi.fizzBuzz()



