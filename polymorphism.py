class Dog:
    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name +' says woof'
class Cat:
    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name +' says meow'
a=Dog('Shepherd')
b=Cat('garfield')
print(a.speak())
print(b.speak())
    
