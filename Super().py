class Animal:
    def animal_sound(self,name):
        self.name=name
        print(f"{self.name} barks")

class Cat(Animal):
    def animal_sound(self, name,breed):
        super().animal_sound(name)
        self.breed= breed
        print(f"{self.name} is a {self.breed}")

cat=Cat()
cat.animal_sound("Rex","Catitutious")