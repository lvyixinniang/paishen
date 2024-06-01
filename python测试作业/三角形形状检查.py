A =int(input())
B =int(input())
C =int(input())

if A+B>C and A+C>B and B+C>A:
    if A==B==C:
        print("等边三角形")
    elif A==B or A==C or B==C:
        print("等腰三角形")

    else:
        print("普通三角形")
else:
    print("不构成三角形")
