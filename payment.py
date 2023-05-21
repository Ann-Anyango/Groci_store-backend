class Payment:
     def __init__(self, amount,date):
          self.amount=amount
          self.date=date

     def process_payment(self):
          print(f"Processing payment of {self.amount} shillings")

     def payment_statement(self):
        print(f"Payment of {self.amount} shillings was made on {self.date}")

payment1 = Payment(500, "2023-05-21")
payment1.process_payment()
payment1.payment_statement()
        # Instance 2
payment2 = Payment(1000, "2023-05-21")
payment2.process_payment()
payment2.payment_statement()





