class Fruits:
    def __init__(self,price,shape,name):
        self.price=price
        self.shape=shape
        self.name=name
    def display(self):
        print(f"My favourite fruits is {self.name} its {self.shape} in shape and cost {self.price} shillings")

# create instance of a class(object)

myobj=Fruits(30,'circle','apple')
myobj.display()


