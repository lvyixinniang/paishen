import csv
import json
with open('movie_inf.in', 'r',encoding='utf-8') as f:
    data = json.load(f)
header = list(data[0].keys())
with open('movie_inf.out', 'w', newline='',encoding='utf-8') as fi:
    writer = csv.writer(fi)
    writer.writerow(header)
    for row in data:
        writer.writerow(row.values())