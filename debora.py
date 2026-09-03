#number 2
length_cm = float(input("Enter a length in centimeters: "))
if length_cm < 0:
    print("Invalid entry: length cannot be negative.")
else:
    length_inches = length_cm / 2.54
    print(length_cm, "cm is equal to", length_inches, "inches")

#number 4
hour = int(input("enter hour (1-12): "))
period = input("enter am or pm: ").lower()
if period == "am":
    hour_24 = hour
else:
    hour_24 = hour + 12
print("The time in 24-hour format is:", hour_24)

#number 6
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
if b == 0:
    print("Error: Division by zero is not possible.")  
else:
    ratio = a / b
    print("The ratio of", a, "and", b, "is:", ratio)

#number 7
import math
num = int(input("Enter a number: "))
root = math.isqrt(num)
if root * root == num:
    print(num, "is a perfect square.")  
else:
    print(num, "is not a perfect square.")   

#number 9
import math
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
if (a + b>c) and (b +c > a) and (a + c > b):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print("The area of the triangle is valid.")
    print("The area of the triangle is:", area)
else:
    print("The area of the triangle is invalid.")

#number 10
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))
if a >= b and a >= c:
    print("The maximum number is:", a)
if b >= a and b >= c:
    print("The maximum number is:", b)
if c >= a and c >= b:
    print("The maximum number is:", c)

#number 11
marital_status = input("Enter marital status (unmarried/married): ").lower()
gender = input("Enter gender (male/female): ").lower()
age = int(input("Enter age: "))
if marital_status == "married":
    print("Eligible for insurance.")
elif marital_status == "unmarried" and gender == "male" and age > 30:
    print("Congratulatins!")
    print("Eligible for insurance.")
else:
    print("We are sorry!")
    print("Not eligible for insurance.")