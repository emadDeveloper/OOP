class House:
    def __init__(self):
        self.window = 5
        self.door = 3

    def view(self):
        print(self.window, 'windows', self.door, 'doors') 


h1 = House()
h2 = House()
h1.view()
h2.view()           