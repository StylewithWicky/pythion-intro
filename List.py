class Users:
    all_Users=[]

    def __init__(self,name):
        self.name=name
        Users.all_Users.append(self)

person1=Users('BOB')
person2=Users('Alice')
person3=Users('John')

for person in Users.all_Users:
    print(person.name)
