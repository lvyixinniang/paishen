def fun(n):
    summ = 0
    if n%2 ==0:
        for i in range(2,n+1,2):
            summ += float(1/i)
        print("%.2f"%summ)
    else:
        for i in range(1,n+1,2):
            summ+=float(1/i)
        print("%.2f"%summ)

try:
    n = input()
    if len(n) != len(str(int(n))) or 1000000 <int(n) or int(n)<=0:
        print("输入不合法! ")
    else:
        fun(int(n))
except:
    print("输入不合法! ")