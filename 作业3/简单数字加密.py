strl = input()
str_num = ""
if strl.isdigit():
    if int(strl)<999:
        print("输入不合法!")
    else:
        for i in range(4):

            # chr()函数需要一个整数作为参数,才能识别到
            # str_num+=str(chr((ord(strl[i])+5)%10))
            str_num+=str((ord(strl[i])+5)%10)

else:
    print("输入不合法!")
#     str_num[::-1] 这种写法是用来反转字符串的
# 其基本形式是 [start:stop:step]。

    # start 是切片的起始位置，默认为0。
    # stop 是切片的结束位置，不包括这个位置上的元素，默认为列表的长度。
    # step 是步长，即每次移动多少位，默认为1。
print(str_num[::-1])