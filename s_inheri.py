class animal:
    def __init__(self, name):
        self.name = name

    def run(self):
        print(self.name, 'is running')


class cat(animal):
    def eat(self):
        print(self.name, 'is eating') 


a1 = animal('foji')
c1 = cat('loki') 
c1.eat()   
c1.run()  
a1.run()
                      