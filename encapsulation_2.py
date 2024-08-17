class Emad:
    def __init__(self,name,id):
        self.name = name 
        self.__id = id

    def view(self):
        print('name:', self.name, 'id:', self.__id)
        self.__method()

    def __method(self):
        print('hoye gese')    


s1 = Emad('roky',66)
s2 = Emad('rony',99)
s1.view() 
s2.view()           