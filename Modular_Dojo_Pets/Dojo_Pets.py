class Pet:
  def __init__(self, name, type, tricks, sound, health=100, energy=50):
    self.name = name
    self.type = type
    self.tricks = tricks
    self.health = health
    self.energy = energy
    self.sound = sound
  
  def sleep(self):
    self.health += 25
    print(f"{self.name} health increased to {self.health}")
    return self
  
  def eat(self):
    self.health += 25
    self.energy += 5
    print(f"{self.name} health and energy increased to {self.health} and {self.energy}")
    return self
  
  def play(self):
    self.health += 10
    self.energy -= 10
    print(f"{self.name} health increased to {self.health}")
    return self
  
  def noise(self):
    print(self.sound)
    return self

class Ninja:
  def __init__(self, first_name, last_name, pet, treats, pet_food):
    self.first_name = first_name
    self.last_name = last_name
    self.pet = pet
    self.treats = treats
    self.pet_food = pet_food
  
  def walk(self):
    self.pet.play()
    print(f"{self.first_name} took their pet {self.pet.name} for a walk.")
    return self
  
  def feed(self, number_of_food=1):
    self.pet.eat()
    print(f"{self.first_name} fed their pet {self.pet.name} {number_of_food} {self.treats}.")
    return self
  
  def bathe(self, is_dirty=False):
    self.pet.noise()
    if (is_dirty):
      is_dirty = True
      self.pet.noise()
      print(f"{self.first_name} gave their pet {self.pet.name} a bath.")
    else:
      print(f"{self.pet.name} is already clean.")
    return self

rango = Pet("Rango", "Chameleon", "Camouflage", "Hiss", 100, 30)

jacob = Ninja("Jacob", "Harris", rango, "Crickets", "Insects")

jacob.walk().feed(3).bathe()