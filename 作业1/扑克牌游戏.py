import random
n = eval(input())
s = eval(input())
rank = {'2':2, '3':3,'4':4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'K': 13, "Q": 12, "J": 11, "A": 14, "okers": 53, "OKERS": 54}
account = [[] for _ in range(n)]
color_level = {"♠":1, "♥":2, "♣":3, "♦":4,"j":5,"J":6}
color = ["♠", "♥", "♣", "♦"]
num = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
poker = [i+j for i in color for j in num]+["jokers", "JOKERS"]
print(f"参与游戏的人数: {n}")
print("新牌的顺序")
print(" ".join(poker))
print("洗牌顺序")
random.seed(s)
random.shuffle(poker)
print(" ".join(poker))
print("每个人手上分到的牌")
for i in range(0,54):
    j = i%n
    account[j].append(poker[i])
for i in  account:
    print(" ".join(i))
print("每个人手上排序的牌")
for i in account:
    i.sort(key=lambda x:(color_level[x[0]],rank[x[1:]]))
    print(" ".join(i))