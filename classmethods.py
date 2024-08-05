class Dog:
    species = "Canis familiaris"
    
    def __init__(self, name):
        self.name = name
    
    @classmethod
    def change_species(cls, new_species):
        cls.species = new_species
    
    @classmethod
    def from_breed(cls, breed):
        return cls(f"A {breed} dog")

dog1 = Dog("Buddy")
dog2 = Dog.from_breed("Golden Retriever")
print(dog1.name)           
print(dog2.name)           
print(dog1.species)         
dog1.change_species("New Species")
print(dog1.species)    
print(dog2.species)        
dog2.change_species("Species")
print(dog2.species)
