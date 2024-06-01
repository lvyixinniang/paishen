dec = float(input())
PI = 0
flag =1
i =1
while 1/i >=dec:
    PI = PI + flag*1/i
    i+=2
    flag = -flag
PI *= 4
print("%.8f" % PI)