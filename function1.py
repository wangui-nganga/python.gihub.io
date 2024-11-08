def lovefood(protein,vegetable,fruit,dessert):
    # data above in the brackets is argument
    print(f"food i enjoy : {protein},{vegetable},{fruit} and {dessert}")
lovefood("chicken","spinach","Apple","Icecream")


def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


def country():
    print(f"I am from Asia")
country()


def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")