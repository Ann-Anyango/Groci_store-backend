
class Product:
   def __init__(self, name, price, description,discount):
       self.name = name
       self.price = price
       self.description = description
       self.discount = discount


   def put_price(self, price):
       self.price = price
    #    sets the price of the product to the provided price value
       print(f"The price of this product is {self.price}")


   def give_discount(self):
       print(f"You have received  a discount {self.discount} shillings")
    # gives out the message indicating that the customer has received a discountof the dicount.


   def change_price(self, amount):
       self.price += amount
       print(f"price changed to {self.price}")

    # updates the pricesof the product of the procduct by adding.
product1 = Product("Skumawiki", 50, "green and fresh", 10)
product1.put_price(55)
product1.give_discount()
product1.change_price(60)