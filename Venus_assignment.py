"""
VENUS
Mbabazi Grace -S26B38/035
Komagum Sidney -S26B38/052
Yawe Jayden John -S26B38/009
Mikisa Faith Deborah -S26B38/038
Munialo David Bradley -S26B38/046

This program basically allows several users to place orders at a campus canteen,
displays meal prices and offers a 10% discount to students only.

"""
while True:
    try:
        n = int(input("How many customers are ordering:"))
        break
    except ValueError:
        print("Invalid input. Please input a whole number")
count = 0
total = 0

for i in range(1,n+1):
    print(f"Customer{i}")
    name = input("Name: ")
    meal_choice = input("Meal choice(St/V/Sp):") #St=Standard, V=Vegeterian, Sp=Special
    student = input("Are you a student(YES/NO):")

    if meal_choice == "St":
        price = 8000
    elif meal_choice == "V":
        price = 7000 
    elif meal_choice == "Sp":
        price = 12000
    else:
        price = 0
        print("invalid meal_choice")
    if student == "YES":
        price = price*0.9

    print(f"This meal is {price} UGX")
    count += 1
    total += price

print(f"The number of orders is {count}")
print(f"The total money collected {total} UGX")