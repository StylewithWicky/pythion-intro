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


class Books:
    library_name="City_library"

    def __init__(self,title,author):
          self.title=title
          self.author=author

    @classmethod
    def change_library_name(cls, new_name):
         cls.library_name= new_name

    def Vitabu(self):
         return f"{self.library_name} has a book by {self.author} it is called {self.title}"
    
Books.change_library_name("National Library")
library1 =Books("The Alchemist","Maitai")
print(library1.Vitabu())

class Restaurant:
    restaurant_place="Mama's Kitchen"

    def __init__(self,dish,prices):
         self.dish=dish
         self.prices=prices


    @classmethod
    def change_restaurant_name(cls ,new_name):
        cls.restaurant_place =new_name

    def show_menu(self):
         return f"{self.restaurant_place} has good food and they charge {self.prices} for {self.dish} "
    
Restaurant.change_restaurant_name("Papa Joe's")
restaurant=Restaurant("Mchele", 350)
print(restaurant.show_menu())
     
          
            