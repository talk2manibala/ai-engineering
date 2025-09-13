class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def birthday(self):
        self.age += 1
        print(f"Happy Birthday {self.name}! You are now {self.age} years old.")

    def is_adult(self):
        return self.age >= 18


if (__name__ == "__main__"):
    p1 = Person("Alice", 30)
    p1.display()
    p1.birthday()
    print(p1.is_adult())

    p2 = Person("Bob", 15)
    p2.display()
    p2.birthday()
    print(p2.is_adult())