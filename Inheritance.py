class phone:
    def call(self):
        print("you  can call")

    def message(self):
        print("you can message")


class cover(phone): 

    def photo(self):
        print("take a photo")

c = cover()
c.call()
c.message()
c.photo()                      