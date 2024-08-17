class student:
    def __init__(self,name,id):
        self.name = name
        self.__id = id

    def details(self):
        print('name:', self.name, 'id:', self.__id)

    def set_id(self,id):
        if(id>0):
            self.__id = id  
        else:
            print('invalid id, enter id again') 

    def get_id(self):
        return self.__id 


    def set_name(self,name):
        self.name = name

    def get_name(self):
        return self.name              



s1 = student('jami',44)
s2 = student('lani',55)
s1.set_id(22)
print(s1.get_id())
s2.set_name('jony')
print(s2.get_name())
s1.details()
s2.details()        
