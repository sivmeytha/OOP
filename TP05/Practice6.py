class Product:
    store_name = "ITC Online Store"
    product_count = 0

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

        Product.product_count += 1

    def display_product(self):
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Quantity: {self.quantity}")
        print(f"Total Value: ${self.total_value()}")

    def total_value(self):
        return self.price * self.quantity

    @classmethod
    def get_product_count(cls):
        return cls.product_count

    @staticmethod
    def is_valid_price(price):
        return price > 0

p1 = Product("Laptop", 800, 5)
p2 = Product("Mouse", 15, 20)
p3 = Product("Keyboard", 30, 10)

print("========== ITC ONLINE STORE ==========\n")

p = [p1, p2, p3]
for i in p:
    i.display_product()
    print("")

total_inventory = (p1.total_value() + p2.total_value() + p3.total_value())

print("\nTotal Products: ", Product.get_product_count())
print("Total Inventory value: $", total_inventory)

