def invoice(name,price,date):
    print(f"Hello {name}")
    print(f"Your total price is {price}")
    print(f"This was on {date}")

invoice("Joe",10.20, 1/10)

def assign_grades(score):
    if score >=90 :
        print('A')
    elif score >= 80 :
       return "A-"
    elif score >= 70 :
        return "A-"
    elif score >= 60 :
        return "B+"
    elif score >= 50 :
         return "B"
    elif score >= 40 :
         return "C-"
    else:
        return "A-"

students =[
    ('Alice',95),
    ('Joe',85),
    ('Alex',75),
    ('Alan',45),
    ('John',5)
    
]
for name, score in students:
    grade=assign_grades(score)
    print(f"{name} : {score} => Grade = {grade}")
