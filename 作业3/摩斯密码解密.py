morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
digit = ['-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']
punctuation = {'.': '.-.-.-', ':': '---...', ',': '--..--', ';': '-.-.-.', '?': '..- -..', '=': '-...-', "'": '.----.', '/': '-..-.', '!': '-.-.--', '-': '-....-', '_': '..--.-', '"': '.-..-.', '(': '-.--.', ')': '-.--.-', '$': '...-..-', '&': '·-···', '@': '.--.-.', ' ': ''}

s = input().split(" ")
real_word = ""
for ch in s:
    if ch in morse:
       real_word += chr(ord('a')+morse.index(ch))
    elif ch in digit:
        real_word += chr(ord('0')+digit.index(ch))
    elif ch in punctuation.values():
        # list[索引值] python的列表的语法
        real_word += list(punctuation.keys())[list(punctuation.values()).index(ch)]
    else:
        real_word += ch
print(real_word)

