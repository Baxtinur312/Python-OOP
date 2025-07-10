class Product:
    def __init__(self, name, price, category, in_stock):
        self.name = name
        self.price = price
        self.category = category
        self.in_stock = in_stock

product1 = Product("Laptop", 12999.99, "electronics", True)
product2 = Product("Mouse", 99.99, "accessories", True)
print(product1.name, "–", product1.price)
print(product2.name, "–", product2.price)