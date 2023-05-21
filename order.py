class Order:
    def __init__(self, customer_id, product):
        self.customer_id = customer_id
        self.product = product
        self.products = []
        self.total_price = 0

    def add_product(self, product_name, price):
        product = {"name": product_name, "price": price}
        self.products.append(product)
        return self.products

    def remove_product(self, product_name):
        for product in self.products:
            if product["name"] == product_name:
                self.products.remove(product)
                print(f"Product '{product_name}' removed from the order.")
            else:
              print(f"Product '{product_name}' not found in the order.")

    def calculate_total_price(self):
        self.total_price = sum(product["price"] for product in self.products)