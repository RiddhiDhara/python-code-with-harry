class animal:
    catagory = "Animal"
class pet(animal):
    subCatagory = "Pet"
    
class dog(pet):
    type = "Dog"
    def bark(self):
        print(f"A {self.type} is a {self.subCatagory} {self.catagory} who barks")

pug = dog()
pug.bark()