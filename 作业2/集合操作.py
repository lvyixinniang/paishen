import random
txt = '''Ifthereisonlyoneargument,itmustbeadictionarymappingUnicode |ordinals(integers)orcharacterstoUnicodeordinals,stringsorNone. |Characterkeyswillbethenconvertedtoordinals. |Iftherearetwoarguments,theymustbestringsofequallength,and |intheresultingdictionary,eachcharacterinxwillbemappedtothe |characteratthesamepositioniny.Ifthereisathirdargument,it |mustbeastring,whosecharacterswillbemappedtoNoneintheresult.'''
lt = list(txt)
x,m1,n1,m2,n2=map(int,input().split())

random.seed(x)
random.shuffle(lt)
# 列表切片（list slicing）操作。这个操作允许你从列表中提取一个子集，
# 即从索引 m1 开始到索引 n1-1 结束（不包括 n1）的所有元素。
# 同样地，lt[m2:n2] 会提取从索引 m2 到 n2-1 的所有元素。
lt1= lt[m1:n1]
lt2 = lt[m2:n2]
# 使用f-string（格式化字符串字面量），将计算出的不同字符数量插入到字符串中打印出来。
print(f"lt1中出现了{len(set(lt1))}个不同的字符")
print(f"lt2中出现了{len(set(lt2))}个不同的字符")
# ' '.join(...)将排序后的字符列表连接成一个字符串，每个字符之间用空格分隔。
# 集运算符&找到同时出现在lt1和lt2中的字符。
print(f"同时出现在lt1和lt2中的字符为：{' '.join(sorted(set(lt1) & set(lt2)))}")
# 集合的差集运算符-找出仅在lt1中出现的字符。
print(f"出现在lt1，但没在lt2中的字符为：{' '.join(sorted(set(lt1)-set(lt2)))}")