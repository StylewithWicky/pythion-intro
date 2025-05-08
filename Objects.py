class Car:
    def __init__(self,make,model):
        self.make=make
        self.model=model

    def speed(self):
        print(f"{self.make} is very fast")

car1= Car("Toyota","Supra")
car2= Car("Mazda","X330")

car1.speed()
car2.speed()