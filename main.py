name=str(input("enter your name "))
marks=int(input("enter your marks"))

with open ("student.csv",'a') as file:
    file.write("f{name},{marks}")

print("student sucessfully added ")


