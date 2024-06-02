import random
txt = '''Ifthereisonlyoneargument,itmustbeadictionarymappingUnicode |ordinals(integers)orcharacterstoUnicodeordinals,stringsorNone. |Characterkeyswillbethenconvertedtoordinals. |Iftherearetwoarguments,theymustbestringsofequallength,and |intheresultingdictionary,eachcharacterinxwillbemappedtothe |characteratthesamepositioniny.Ifthereisathirdargument,it |mustbeastring,whosecharacterswillbemappedtoNoneintheresult.'''
list1 = list(txt)
x,m,n=map(int,input().split())

random.seed(x)
random.shuffle(list1)

Dict1 = {}
for ch in list1:
    Dict1[ch] = Dict1.get(ch,0)+1

SortDict = sorted(Dict1.items(),key=lambda x:x[1],reverse=True)

for i in range(0,5):
    print("{}:{}".format(SortDict[i][0],SortDict[i][1]))