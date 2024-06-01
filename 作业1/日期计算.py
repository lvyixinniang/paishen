import datetime
a = input().split("-")
d1 = datetime.datetime(int(a[0]),int(a[1]),int(a[2]))
# print(d1)
d2 = datetime.datetime(int(a[0]),1,1)
# print(d2)
print((d1-d2).days+1)