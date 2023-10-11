Name = str(input("Hello, what is your name?"))
print("Hello,", Name, ",Good to meet you!")

Celsius = float(input("Enter a temperature in Celsius:"))
Fahrenheit = (Celsius*9/5)+32
print(Celsius, "C", "is equivalent to", Fahrenheit, "F")

students = int(input("How many students?"))
G_size = int(input("Required group size?"))
groups = (students // G_size)
remainders = (students % G_size)
if remainders == 1:
    print("There will be", groups, "groups with", remainders, "student left over")
else:
    print("There will be", groups, "groups with", remainders, "students left over")

sweets = int(input("How many sweets do you have in the tub"))
attendance = int(input("How many students attended the class"))
given = (sweets // attendance)
left = (sweets % attendance)
print("Each student will get", given, "sweets each and you will have", left, "left over")


