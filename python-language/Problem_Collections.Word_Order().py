from collections import OrderedDict
n = int(input())
words = OrderedDict()
for i in range(n):
     a = input()
     if a in words:
        words[a]+=1
     else:
        words[a]=1
val = list()           
print(len(words.keys()))
for k,v in words.items():
    val.append(v)
print(*val)    
