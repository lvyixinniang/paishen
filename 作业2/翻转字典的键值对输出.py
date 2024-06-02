try:
    d = eval(input())
    reverse_dict = dict(zip(d.values(),d.keys()))
    print(reverse_dict)
except:
    print("输入错误")