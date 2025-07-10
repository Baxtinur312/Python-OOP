class Product:
    def __init__(self, name, price, category, in_stock):
        self.name = name
        self.price = price
        self.category = category
        self.in_stock = in_stock

    def info(self):
        stock_status = "In stock" if self.in_stock else "Out of stock"
        print(f"{self.name} - {self.price} so'm, Category: {self.category}, Status: {stock_status}")

def task15():
    p1 = Product("Smartphone", 250.0, "electronics", True)
    p2 = Product("TV", 500.0, "electronics", False)
    p3 = Product("Blender", 80.0, "home", True)
    p4 = Product("Mouse", 20.0, "computer", True)
    p5 = Product("Headphones", 45.0, "accessory", False)

    products = [p1, p2, p3, p4, p5]
    total = sum(p.price for p in products if p.in_stock)
    print(f"Ombordagi mahsulotlar narxi: {total}")