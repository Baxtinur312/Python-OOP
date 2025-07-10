class Product2:
    def __init__(self, name, price, category, in_stock):
        self.name = name
        self.price = price
        self.category = category
        self.in_stock = in_stock

    def check_stock(self):
        if self.in_stock:
            print(f"{self.name} omborda mavjud ")
        else:
            print(f"{self.name} hozirda tugagan ")

p1 = Product2("AirPods", 199.99, "electronics", True)
p2 = Product2("iPhone 13", 999.99, "electronics", False)
p1.check_stock()
p2.check_stock()
