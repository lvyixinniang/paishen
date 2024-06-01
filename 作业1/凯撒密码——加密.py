str1 = input()
for i in range(0,len(str1)):
    if "X"<= str1[i] <="Z" or "x"<=str1[i]<="z":
        print(chr(ord(str1[i])-23),end="")
    elif "7" <= str1[i] <="9":
        print(chr(ord(str1[i])-7),end="")
    elif str1[i]==" ":
        print(" ",end="")
    else:
        print(chr(ord(str1[i])+3),end="")

# print("X=%d" %ord("X"))
# print("Z=%d" %ord("Z"))
# print("a=%d" %ord("a"))
# print("z=%d" %ord("Z"))
# print("1=%d" %ord("1"))