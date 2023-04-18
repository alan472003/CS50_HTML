class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def __str__(self):
        return "Name: " + self.name + ", Age: " + str(self.age)
    
    def __repr__(self):
        return "Name: " + self.name + ", Age: " + str(self.age)
    
    Animal = pig("Pig", 5)
    print(pig)
    print(pig.__repr__())
    print(pig.__str__())
    print(pig.get_name())
    print(pig.get_age())
    Animal.set_name("Dog")
    Animal.set_age(10)
    print(Animal.get_name())
    print(Animal.get_age())
    print(Animal)
    print(Animal.__repr__())
    print(Animal.__str__())
