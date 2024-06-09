m,n = map(int,input().split())
# 使用input()函数获取用户输入的一个字符串，然后使用split()方法将其拆分为多个字符串，
# 并使用map()函数将这些字符串转换为整数类型。最终，将这些整数赋值给变量m和n。
def isPrime(n):
    if n == 1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def isEmirp(n):
    if str(n)==str(n)[::-1]:
        return False
    if isPrime(n):
        n = str(n)
        n = str[::-1]
        n = int(n)
        if isPrime(n):
            return True
        else:
            return False

for i in range(m,n+1):
    if isEmirp(i):
        print(i,end=' ')