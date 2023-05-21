# class Payment:
#      def __init__(self,date,balance):
#           self.date=date
#           self.balance = balance

#      def process_payment(self,amount):
#          self.balance-=amount
#          print(f"Processing payment of {amount} shillings your account balance is {self.balance} ")


# payment1 = Payment( "2023-05-21", 1000)
# payment1.process_payment(500)
#         # Instance 2
# payment2 = Payment( "2023-05-21",2000)
# payment2.process_payment(600)




class Stock:
 def __init__(self, product, quantity,price):
     self.product = product
     self.quantity = quantity
     self.price = price


 def generate_purchase_order(self):
       print(f"Added {self.quantity} kgs of {self.product} worth {self.price*self.quantity}")


 def remove_stock(self, removed_quantity):
    if self.quantity >= removed_quantity:
        self.quantity -= removed_quantity
        print(f"Removed {removed_quantity} kgs of {self.product}. New stock quantity: {self.quantity} kgs.")
    else:
        print("Insufficient stock. Cannot remove requested quantity.")
      


 def check_stock_level(self):
     if self.quantity>2000:
         print("stock is updated")
     else:
         print("stock needs to be updated")


 def update_quantity(self, new_quantity):
    self.quantity = new_quantity
    print(f"Updated quantity of {self.product} to {self.quantity} kgs.")


 def check_availability(self, required_quantity):
    if self.quantity >= required_quantity:
        print(f"{required_quantity} kgs of {self.product} are available in stock.")
    else:
        print(f"Only {self.quantity} kgs of {self.product} are available in stock. Insufficient quantity.")

stock1 = Stock("Banana", 1340, 100)
stock1.generate_purchase_order()
stock1.remove_stock(350)
stock1.check_stock_level()
stock1.update_quantity(1560)
stock1.check_availability(1400)