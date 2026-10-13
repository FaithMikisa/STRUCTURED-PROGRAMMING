marks = [90, 80, 70, 60, 50, 44, 30, 20, 10]
def pass_rate(marks, threshold  = 50):
    if len(marks) == 0:
        return 0
    passed = 0
    for m in marks:
        if m >= threshold:
            passed = passed + 1
    return (passed / len(marks)) * 100

print("Pass rate %:", pass_rate(marks))  # Output: 100.0
print("Distinction %:", pass_rate(marks, 80))  # Output: 80.0