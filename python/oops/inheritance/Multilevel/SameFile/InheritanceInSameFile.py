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
    
class Profession(Person):
    def __init__(self, name, age, profession):
        super().__init__(name, age)
        self.profession = profession

    def display_profession(self):
        print(f"{self.name} is a {self.profession}.")

class Experience(Profession):
    def __init__(self, name, age, profession, years_experience):
        super().__init__(name, age, profession)
        self.years_experience = years_experience

    def display_experience(self):
        print(f"{self.name} has {self.years_experience} years of experience as a {self.profession}.")  
        self.display()
        self.display_profession()
        self.birthday()
        print(self.is_adult())
        print(f"Is adult: {self.is_adult()}")

if __name__ == "__main__":
    exp1 = Experience("Diana", 35, "Designer", 10)
    exp1.display_experience()