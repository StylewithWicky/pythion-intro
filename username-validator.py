import re

def user_name(username):
    

    if not ( 4 <= len(username) <= 25):
     return False
   
  
    pattern = r'^[a-zA-Z][a-zA-Z0-9_]*[a-zA-Z0-9]$'
    return bool(re.match(pattern, username)) 

example_username=['Joedoe','alex231','amtoocoolforthis']
for name in example_username :
    print(f"{name}: {user_name(name)}")

