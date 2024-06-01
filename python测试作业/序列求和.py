m = int(input())
n = int(input())
num = 0
for i in range(m,n+1):
    if i%5==0 and i%7==0:
        num +=i
print(num)
