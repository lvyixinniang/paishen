# 创建了 salary.in 和 salary.out文件

fr = open("salary.in",'r',encoding='utf-8')
fw = open("salary.out",'w',encoding='utf-8')
lst = []
for line in fr:
    line = line.replace('\n', '')
    lst.append(line.split(','))
fr.close()

lst[0].append("一季度总收入")
for i in range(1, len(lst)):
    total_income = 0
    for j in range(1, len(lst[i])):
        total_income += int(lst[i][j])
    lst[i].append(str(total_income))

    # reverse = True: 这是sorted()函数的另一个参数，当设置为True时，列表将以降序（从大到小）排序。默认情况下，sorted()按升序（从小到大）排序。
lst[1:] = sorted(lst[1:], key=lambda x: int(x[-1]), reverse=True)
for item in lst:
    fw.write(','.join(item) + '\n')
fw.close()