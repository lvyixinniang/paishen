ls = [eval(i) for i in input().split(" ")]
for i in ls:
    a =2
    while a**2<i:
        if i%a==0:
            break
        elif (a+1)**2>=i:
            print(end = f"{i} ")
        a+=1