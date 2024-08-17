class my_calculator:
    def product(self,*nums):
        sum =  1
        for i in nums:
            sum = sum * i
        print(sum) 


c1 = my_calculator()
c1.product(3,4,5,8,9)           