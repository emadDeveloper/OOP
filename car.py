class car:
    def __init__(self,name,model):
        self.name = name
        self.model_year = model
        self.wheel = 4

    def view(self):
        print('the model year of this', self.name, 'is', self.model_year)



c1 = car('BMW', 2017) 
c2 = car('prado',2010)  
c1.view() 
c2.view() 
print(c1.__dict__)       