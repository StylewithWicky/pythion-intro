class Car:
    wheels=4
    def __init__(self,name):
        self.name =name

    @classmethod
    def change_wheels(cls,new_wheels):
            cls.wheels =new_wheels

    def drive(self):
         return f"{self.name} is now driving on {self.wheels}"

Car.change_wheels(6)
car1 =Car('Volvo')

print(f"This {car1.name} has {car1.wheels} wheels. ")
print(car1.drive())
            