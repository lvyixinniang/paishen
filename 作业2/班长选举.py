count_dict = {}
for i in range(8):
    name = input()
    count_dict[name] = count_dict.get(name,0)+1
max =0
mname = " "
for key,value in count_dict.items():
    if value > max:
        max = value
        mname = key
print(mname,max)