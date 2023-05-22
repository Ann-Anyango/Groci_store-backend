class Customer:
    shop = "Groci_store"
    def __init__(self,name, email, transaction,loyalty_points):
        self.name = name
        self.email = email
        self.transaction = transaction
        self.loyalty_points = loyalty_points
        self.cart = []
    def signup():
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        transaction = input("Enter your transaction ID: ")
        loyalty_points = (input("Enter your loyalty points: "))
        return Customer(name, email, transaction, loyalty_points)
    def login():
        email = input("Enter your email: ")
        transaction = input("Enter your transaction ID: ")
        loyalty_points = (input("Enter your loyalty points: "))
        return Customer("",email, transaction, loyalty_points)
customer1 = Customer.signup()
print(f"Sign up successful for {customer1.name}. Welcome to {customer1.shop}!")
customer2 = Customer.login()
print(f"Login successful for {customer2.name}. Welcome back to {customer2.shop}!")