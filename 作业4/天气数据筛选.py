import csv


with open('weather.in', encoding='utf-8',newline='') as fr:
    reader = csv.reader(fr)
    with open('weather.out', 'w', encoding='utf-8', newline='') as fw:
        fw.write("日期,天气状况,最高温,最低温,风力风向\n")
        writer = csv.writer(fw)
        for row in reader:
            if row[1] == '阴' and int(row[3].replace('℃', '').strip()) >= 1:
                writer.writerow(row)
