
class Stock:
 def __init__(self, product, quantity):
     self.product = product
     self.quantity = quantity


 def generate_purchase_order(self):
       print(f"Added {self.quantity} kgs of {self.product}.")


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