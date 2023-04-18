from bank.models import User, Deposit


user1 = User()

user1.check_balance()

deposit1 = Deposit()
user1.withdraw()

user1.check_balance()