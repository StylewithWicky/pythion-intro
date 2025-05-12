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

class Vehicle:
    def __init__(self,name):
        self.name=name
        print(f"{self.name} goes vroom")

class Car(Vehicle):
    def __init__(self, name,speed):
        super().__init__(name)
        self.speed=speed
        print(f"{self.name} goes from {self.speed} in 3 seconds")

car=Car("Nissan 350z","0 -60")
car.speed