def task18():

    pr1 = Product("TV", 500, "electronics", True)
    pr2 = Product("Phone", 800, "electronics", True)
    pr3 = Product("Laptop", 1200, "computer", True)
    pr4 = Product("Watch", 300, "accessory", True)
    pr5 = Product("Tablet", 600, "electronics", True)
    pr6 = Product("Speaker", 150, "audio", True)

    products = [pr1, pr2, pr3, pr4, pr5, pr6]
    most_expensive = max(products, key=lambda p: p.price)
    print("Eng qimmat mahsulot:")
    most_expensive.info()
class Product:
    def __init__(self, name, price, category, in_stock):
        self.name = name
        self.price = price
        self.category = category
        self.in_stock = in_stock

    def info(self):
        stock_status = "In stock" if self.in_stock else "Out of stock"
        print(f"{self.name} - {self.price} so'm, Category: {self.category}, Status: {stock_status}")