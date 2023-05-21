class Payment:
     def __init__(self, amount,date):
          self.amount=amount
          self.date=date

     def process_payment(self):
          print(f"Processing payment of {self.amount} shillings")

     def payment_statement(self):
        print(f"Payment of {self.amount} shillings was made on {self.date}")