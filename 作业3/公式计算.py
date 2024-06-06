m = int(input())
result = 1
factorial = 1
for i in range(1, m+1):
    factorial *= i
    result += factorial
print(result)