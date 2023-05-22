class Customer:
    def __init__(self, first_name, second_name, email, password):
        self.first_name = first_name
        self.second_name = second_name
        self.email = email
        self.password = password
    def signup():
        first_name = input("Enter your first name: ")
        second_name = input("Enter your second name: ")
        email = input("Enter your email: ")
        password = input("Enter password: ")
        confirm_password = input("Confirm password: ")
        while password != confirm_password:
            print("Passwords do not match.")
            password = input("Enter password: ")
            confirm_password = input("Confirm password: ")
        return Customer(first_name, second_name, email, password)
    def login():
        email = input("Enter your email: ")
        password = input("Enter password: ")
        return Customer("", "", email, password)
customer1 = Customer.signup()
print(f"Sign up successful for {customer1.first_name}. Welcome to Groci store!")
customer2 = Customer.login()
print(f"Login successful for {customer2.email}. Welcome back to Groci store!")







