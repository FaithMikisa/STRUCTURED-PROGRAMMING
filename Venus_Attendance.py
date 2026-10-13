"""
MIKISA FAITH S26B38/038
YAWE JAYDEN JOHN S26B38/009
MUNIALO DAVID BRADLEY S26B38/046
MBABAZI GRACE S26B38/035
KOMAGUM SIDNEY S26B38/052
"""
def safe_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('Invalid input.Enter an integer!!!')

def grade(mark):
    if mark>=50:
        return "Pass"
    return "Fail"

def valid_name(name):
    return name.replace(" ", "").isalpha() #.replace removes the spaces in the middle so that Name spacing is allowede eg(Yawe Jayden)
# The .isalpha() returns True only if every character is a letter thus digits and Letters with symbols/digits are rejected eg(Faith@,John2,34)

names=[]
attendance=[]
marks=[]

#Collecting data
count=safe_int("How many students to process?:") 
while count<1: #This is to cater for invalid input
    print("Enter a number greater than 0") 
    count=safe_int("How many students to process?:")

for i in range(1,count+1 ):
    print(f"Student{i}")

    name=input("Name: ")
    while not valid_name(name):
        print("Invalid name.Use letters")
        name=input("Name: ")
    while name=="":
        print("Enter your name please!!")
        name=input("Name: ")

    att=input("Attendance (P/A): ").upper()
    while att!="P" and att!="A": # != (Means is not equal to)
        print("Invalid,Enter P or A only")
        att=input("Attendance (P/A): ")

    mark=safe_int("Mark(0-100): ")
    while mark<0 or mark>100:
        print("Invalid.Mark must be between 0 and 100")
        mark=safe_int("Mark(0-100): ")

    names.append(name)
    attendance.append(att) 
    marks.append(mark)  

print("====SESSION SUMMARY====")
passed=0
failed=0

for i in range(len(marks)):
    result=grade(marks[i])
    print(names[i],attendance[i],marks[i],result)
    if result=="Pass":
        passed +=1
    else:
        failed+=1

print("Present: ",attendance.count("P"))
print("Absent: ",attendance.count("A"))        
print("Average mark: ",sum(marks)/count)
print("Passed: ",passed)
print("Failed: ",failed)


   



