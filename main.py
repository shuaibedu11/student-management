name=str(input("enter the student name :"))
marks=int(input("enter the student marks :"))

with open("student.csv","a")as file:
    file.write(f"{name},{marks}/n")

print("student add sussessfully")
