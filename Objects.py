#Instance variables
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


#Class variables
class dog:
    species="cannibas mutisya"


    def __init__(self,name):
        self.name=name 

dog1=dog("Bosco")
dog2=dog("Janet")

print(dog1.species)

#Getter and Setter

class house:
    def __init__(self,name):
        self.name=name

    @property
    def name(self):
        return self._name  #getter
    



#noma

    @name.setter
    def name(self,new_name):
        if not new_name:
            raise ValueError('Name cannot be empty')
        
        self.name=new_name
        

