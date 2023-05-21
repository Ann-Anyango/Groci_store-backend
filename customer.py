class Customer:
    shop = "Groci_store"
    def __init__(self,name, email, transaction,loyalty_points):
        self.name = name
        self.email = email
        self.transaction = transaction
        self.loyalty_points = loyalty_points
        self.cart = []
    
    def add_to_cart(self,item):
        self.cart.append(item)
        print(f"{self.cart}")
        
    def remove_from_cart(self, item):
        if item in self.cart:
            self.cart.remove(item)
            print(f"Item {item} removed from cart.")
        else:
            print(f"Item {item} not found in cart.")

    def get_transaction(self):
        print (f"Trasaction for {self.name} of {self.transaction} is successful ")
        
    def add_points(self):
        print(f"Thank you for shopping with Groci store, you have received {self.loyalty_points} points")
        

