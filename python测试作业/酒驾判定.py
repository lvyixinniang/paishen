s = int(input())
if s<20:
    print("不构成饮酒驾驶行为，可以开车，但要注意安全!")
elif 20<=s<80:
    print("已构成饮酒驾驶行为，请不要开车!")
elif 80<=s:
    print("已构成醉酒驾驶行为，千万不要开车!")