# 此题需要两个文件 , 充当输入输出
# 即 data.in 和 data.out
fr = open('data.in','r',encoding='utf-8')
fw = open('data.out','w',encoding='utf-8')

for line in fr:
    if line[0] == "姓":
        line = line.replace(line[3:5], "*"*len(line[3:5]))
        line = line[3:6][::-1]
        fw.write("姓名: "+ line + '\n')
    elif line[0] == '身':
        line = line.replace(line[11:19],"*"*len(line[11:19]))
        fw.write(line)
    elif line[0] == "手":
        line = line.replace(line[7:11] , "*"*len(line[7:11]))
        fw.write(line)
fr.close()
fw.close()