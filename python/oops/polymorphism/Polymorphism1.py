class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
    
class Profession(Person):
    def __init__(self, name, age, profession):
        super().__init__(name, age)
        self.profession = profession

    def display(self):
        super().display()
        print(f"Profession: {self.profession}")


class Experience(Profession):
    def __init__(self, name, age, profession, years_experience):
        super().__init__(name, age, profession)
        self.years_experience = years_experience

    def display(self):
        super().display()
        print(f"Years of Experience: {self.years_experience}") 

if __name__ == "__main__":
    mr = Experience("Alice", 30, "Engineer", 5)
    mr.display()