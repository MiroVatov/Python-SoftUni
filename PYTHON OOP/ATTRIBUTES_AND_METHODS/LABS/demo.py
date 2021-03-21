from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)

    def display(self):
        print(self.name + "'s age is: " + str(self.age))


person_two = Person("Dido", 44)
person = Person.from_birth_year('John',  1985)
person.display()  # John's age is: 35
person_two.display()