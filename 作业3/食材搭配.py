# input土豆$土豆$茄子$洋葱%洋葱*土豆&芹菜
# output土豆+洋葱 土豆+芹菜 土豆+茄子 洋葱+芹菜 洋葱+茄子 芹菜+茄子

str1 = input()
each_food = ""
food = {}
for ch in str1:
    # 字符的Unicode编码是否小于2000
    if ord(ch) <2000:
        food[each_food] = 0
        each_food = ""
    else:
        each_food+=ch
food[each_food] = 0
# 将字典的键转换为列表
food = list(food.keys())
food.sort(key=lambda x: int(ord(x[0])))
food_match =[]
for i in range(len(food)):
    for j in range(i+1,len(food)):
        food_match.append(food[i]+"+"+food[j])
# key 参数使用了一个 lambda 函数。
# x: 这是 lambda 函数的一个参数，代表 food_match 列表中的每一个元素
# lambda x: int(ord(x[0])): 整个 lambda 函数的意思就是：
# “对于列表中的每一个元素 x，计算并返回 x 第一个字符的 Unicode 编码”。
food_match.sort(key=lambda x: int(ord(x[0])))
for ch in food_match:
    print(ch,end=' ')


# python三种数据结构的特性:
# 元组 : 有序,不可变 , 元素可重复
# 字典 : 无序,键值对,可变,建的唯一性,查找速度快
# 列表 : 有序,可变,元素可重复