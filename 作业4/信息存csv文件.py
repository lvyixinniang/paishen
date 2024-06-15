fr = open('inf.in', 'r', encoding='utf-8')
fw = open('inf.out', 'w', encoding='utf-8')
fw.write("姓名,手机号,身份证号,居住地\n")
info = {}
count = 0

for line in fr:
    key, value = line.split("：")
    key = key.strip()
    value = value.strip()
    info[key] = value

    count += 1
    if count == 4:
        fw.write(f"{info['姓名']},{info['手机号']},{info['身份证号']},{info['居住地']}\n")
        count =0
        info = {}
fr.close()
fw.close()