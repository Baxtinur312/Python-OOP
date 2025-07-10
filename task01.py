class Car:
    def __init__(self, model, brand, year):
        self.model = model
        self.brand = brand
        self.year = year

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"

car = Car("X5", "BMW", "2022")
print(car)
