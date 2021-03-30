class Lion:

    def __init__(self, name: str, gender: str, age: int):
        self.name = name
        self.age = age
        self.gender = gender

    def get_needs(self):
        return 50

    def length(self):
        return self.length

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

