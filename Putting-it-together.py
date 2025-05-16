import re
#Hii naeka ndio niokoe streek
#I really need to be serious with this tuff
class User :
    all_user=[]
    user_count=0

    def __init__(self,name,email):
        if not self.validate_email(email):
            raise ValueError("Invalid email email")
        
        self.name=name
        self.email=email
        self.role="User"
        User.user_count=+1
        User.all_user.append(self)
    def display(self):
        return f"{self.role} | Name:{self.name} | Email :{self.email}"
