class data:
    def __init__(self,x):
        self.x = x

    def __add__(self,other):
        return self.x + other.x


num1 = data(22)
num2 = data(22)
str1 = data('john') 
str2 = data('21')       
print(num1+num2)
print(str1+str2)