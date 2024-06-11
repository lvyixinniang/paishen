secret_key = input().lower()
plain_text = input()
upper_words = []
lower_words = []
num_words =[]

for i in range(26):
    # 就是一个使用了列表推导式的例子。不清楚语法的 注意:其中chr((i + j) , 既有i ,又有j
    upper_letter = [chr((i + j) % 26 + 65) for j in range(26)]
    upper_words.append(upper_letter)
    lower_letter = [chr((i + k) % 26 + 97) for k in range(26)]
    lower_words.append(lower_letter)
for i in range(10):
    num_letter = [chr((i + j) % 10 + 48) for j in range(10)]
    num_words.append(num_letter)
row = 0  # 行
for ch in plain_text:
    # 检查字符串中的所有字母是否都是小写
    if ch.islower():
        print(lower_words[ord(secret_key[row % len(secret_key)]) - 97][ord(ch) - 97], end='')
    elif ch.isupper():
        print(upper_words[ord(secret_key[row % len(secret_key)]) - 97][ord(ch) - 65], end='')
    elif ch.isdigit():
        print(num_words[(ord(secret_key[row % len(secret_key)]) - 97) % 10][ord(ch) - 48], end='')
    else:
        print(ch, end='')
        row -= 1
    row += 1
