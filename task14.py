class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def info(self):
        print(f"{self.name}, {self.age} yoshda, {self.grade}-sinf o‘quvchisi.")

def task14():
    s1 = Student("Ali", 15, 9)
    s2 = Student("Vali", 17, 11)
    s3 = Student("Sami", 16, 10)
    s4 = Student("Olim", 14, 8)
    s5 = Student("Aziz", 18, 11)

    students = [s1, s2, s3, s4, s5]
    oldest = max(students, key=lambda s: s.age)
    oldest.info()
