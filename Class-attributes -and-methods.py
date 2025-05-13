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


     
          
            