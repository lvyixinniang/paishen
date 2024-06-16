import random

txt = '''Ifthereisonlyoneargument,itmustbeadictionarymappingUnicode |ordinals(integers)orcharacterstoUnicodeordinals,stringsorNone. |Characterkeyswillbethenconvertedtoordinals. |Iftherearetwoarguments,theymustbestringsofequallength,and |intheresultingdictionary,eachcharacterinxwillbemappedtothe |characteratthesamepositioniny.Ifthereisathirdargument,it |mustbeastring,whosecharacterswillbemappedtoNoneintheresult.'''
List = list(txt)  # 将字符串转换为列表

x, m, n = map(int, input().split())  # 输入随机种子x和区间范围m和n

random.seed(x)  # 设置随机种子
random.shuffle(List)  # 打乱列表顺序

List1 = List[m:n + 1]  # 获取m到n之间的区间

Dict1 = {}  # 创建一个空字典用于统计字符出现次数
for ch in List1:
    Dict1[ch] = Dict1.get(ch, 0) + 1

SortDict = sorted(Dict1.items(), key=lambda x: x[1], reverse=True)  # 按出现次数排序

for i in range(0, 5):
    print("{}:{}".format(SortDict[i][0], SortDict[i][1]))  # 输出前5个字符和次数