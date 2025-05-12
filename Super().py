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

class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def display_info(self):
        print(f"Name: {self.name}, ID: {self.id}")

    def calculate_salary(self):
        return 50000  
    
class Manager(Employee):
    def __init__(self, name, id,department):
        super().__init__(name, id)
        self.department=department
    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")
    def calculate_salary(self):
        base =super().calculate_salary()
        return base +20000
    
class Teacher(Employee):
    def __init__(self, name, id,subject):
        super().__init__(name, id)
        self.subject =subject
    def display_info(self):
        super().display_info()
        print(f"Subject : {self.subject}")
    def calculate_salary(self):
        base =super().calculate_salary()
        return base +3000
    
emp = Employee("Alice", 101)
mgr = Manager("Bob", 102, "HR")
teach= Teacher("Angel",101,"CRE")

print("\n--- Employee ---")
emp.display_info()
print(f"Salary: ${emp.calculate_salary()}")

print("\n--- Teacher ---")
teach.display_info()
print(f"Salary: ${teach.calculate_salary()}")

print("\n--- Manager ---")
mgr.display_info()
print(f"Salary: ${mgr.calculate_salary()}")
        