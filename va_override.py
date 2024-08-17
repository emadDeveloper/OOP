class animal:
    def __init__(self,name):
        self.name = name
        self.color = 'black'

    def eat(self):
        print(self.color, self.name, 'was eating')


class dog(animal):
    def __init__(self,name,color):
        super().__init__(name)
        self.color = color

    def bark(self):
        print(self.color, self.name, 'was barking')


d1 = dog('lobit','white')
d1.bark() 
d1.eat()                       