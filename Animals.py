class Animal:
    def __init__(self, name):
        self.name = name 
    def speak(self):
        return f'{self.name} says rahh!'
    def reply(self):
       return self.speak()

class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)
    def speak(self):
        return f'{self.name} says moo!'

class Cat(Mammal):
    def __init__(self, name):
        super().__init__(name)
    def speak(self):
        return f'{self.name} says Meow!'

class Dog(Mammal):
    def __init__(self, name):
        super().__init__(name)
    def speak(self):
        return f'{self.name} says woof!'

class Primate(Mammal):
    def __init__(self, name):
        super().__init__(name)
    def speak(self):
        return f'{self.name} says ooga!'

class ComputerScientist(Primate):
    def __init__(self):
        super().__init__()

if __name__ == '__main__':
    c1 = Cat('babs')
    print(c1.speak())
    print(c1.reply())
