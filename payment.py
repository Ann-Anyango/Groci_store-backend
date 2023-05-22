
class Payment:
    def __init__(self, date, balance):
        self.date = date
        self.balance = balance
    def process_payment(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"You have paid {amount} shillings for 7kgs of oranges, and your new balance is {self.balance} shillings"
        else:
            return f"Your balance is {self.balance} shillings. You cannot purchase oranges."
    def payment_statement(self, amount):
        return f"Payment of {amount} shillings was made on {self.date}. Remaining balance is {self.balance} shillings"
loyalty_points = (input("Enter your loyalty points: "))

# first Instance
payment1 = Payment("2023-05-21", 1000)
print(payment1.process_payment(700))
print(payment1.payment_statement(600))
# second Instance
payment2 = Payment("2023-05-21",800)
print(payment2.process_payment(1000))
print(payment2.payment_statement(200))





