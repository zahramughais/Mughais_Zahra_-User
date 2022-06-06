class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received
    # make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    # display_user_balance(self) - have this method print the user's name and account balance to the terminal
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
    # BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and 
    # add that amount to other other_user's balance
    def transfer_money(self, other_user, amount):
        other_user.account_balance += amount
        self.account_balance -= amount

zahra = User('Zahra','zahra@gmail.com')
lady_gaga = User('lady gaga', 'gaga@gmail.com')
marwa = User('marwa', 'cayoot@gmail.com')

zahra.make_deposit(4000)
zahra.make_deposit(2000)
zahra.make_deposit(2000)
zahra.make_withdrawal(300)
zahra.display_user_balance()

lady_gaga.make_deposit(220000)
lady_gaga.make_deposit(150)
lady_gaga.make_withdrawal(450)
lady_gaga.make_withdrawal(1500)
lady_gaga.display_user_balance()

marwa.make_deposit(5000)
marwa.make_withdrawal(2000)
marwa.make_withdrawal(400)
marwa.make_withdrawal(290)
marwa.display_user_balance()

zahra.transfer_money(marwa, 1000)
zahra.display_user_balance()
marwa.display_user_balance()