class Human:
  species = "Homo Sapiens" #Class Variable

  #Constructor
  def __init__(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender

#Object
x = Human("Edcorner", 30, "Male")
y = Human("Learning", 32, "Female")

print(x.species)
print(y.species)

print(f"Hi! My name is {x.name}. I am a {x.gender}, and I am {x.age} years old")
print(f"Hi! My name is {y.name}. I am a {y.gender}, and I am {y.age} years old")