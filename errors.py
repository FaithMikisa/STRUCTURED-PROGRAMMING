try:
    a = int(input("First number: "))
    b = int(input("Second number: "))
    print("Result:", a / b)
except ValueError:
    print("Please enter valid numbers.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("success")
finally:
    print("accomplished")


# while True:
#         try:
#             age = int(input("Enter your age: "))
#             break   #leave the loop if conversion worked
#         except ValueError:
#             print("Please enter a whole number.")
# print("Age recorded:", age)