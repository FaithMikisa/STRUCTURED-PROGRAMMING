n = 0   
while n <= 10:
    print(n)
    n+=1

n =10
while n > 0:
    print(n)
    n -= 1

for i in range(3):
    for j in range(4):
        print(i, j)

n = int(input('enter number: '))
sum = 0
for i in range(1, n+1):
    sum += i
    print(sum)