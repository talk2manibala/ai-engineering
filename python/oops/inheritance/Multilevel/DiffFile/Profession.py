
from Person import Person
class Profession(Person):
    def __init__(self, name, age, profession):
        super().__init__(name, age)
        self.profession = profession

    def display_profession(self):
        print(f"{self.name} is a {self.profession}.")

if __name__ == "__main__":
    p1 = Profession("Alice", 30, "Engineer")
    p1.display()
    p1.display_profession()
    p1.birthday()
    print(p1.is_adult())