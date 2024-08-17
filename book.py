class Book:
    def __init__(self,name,author):
        self.name = name
        self.author = author
        self.price = 0

    def set_price(self,price):
        self.price = price

    def get_price(self):
        return self.price

    def details(self):
        print('book name', self.name, 'author', self.author, 'price', self.price)


b1 = Book('oporichita','tagore') 
b1.set_price(189)  
b1.details()             