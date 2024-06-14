# 本章 , 需要先创建 两个文件 , moive.in 和 movie.out

import json

fr = open('movie.in','r',encoding='utf-8')
fw = open('movie.out','w',encoding='utf-8')

list1 = []
for line  in fr:
    line = line.replace("\n","")
    list1.append(line.split(" "))
fr.close()
for i in range(1,len(list1)):
    # 使用zip()函数将第一个元素和当前元素对应的部分打包成一个元组，然后
    # 使用dict()函数将元组转换为 字典。将转换后的字典赋值给列表list1中当前的元素
    list1[i] = dict(zip(list[0],list[i]))

#     使用JSON模块的 dump()函数 将列表list1 中从索引1开始到最后的部分转换为 JSON格式，
#     并将结果写入到文件fw中。参数indent=4 指定缩进为4个空格，
#     ensure_ascii=False表示不对非ASCII字符进行转义。
json.dump(list1[1:],fw,indent=4,ensure_ascii=False)
fw.close()