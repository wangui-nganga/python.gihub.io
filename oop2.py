
class People:
    def __init__(self ,name ,age ,gender):
        self.name =name
        self.age =age
        self.gender =gender
    def display(self):
        print(f"My name is {self.name} my age is {self.age} and i identify as {self.gender}")

    # create instance of a class (object)
myobj =People('Mike' ,23 ,'Male')
myobj.display()