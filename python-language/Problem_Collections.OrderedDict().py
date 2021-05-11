from collections import OrderedDict

n = int(input())
item_list = OrderedDict()
for i in range(n):
    a = input()
    b = a.split()
    c = b[len(b)-1]
    d = a.replace(c,'')
    if d in item_list:
        item_list[d]+= int(c)
    else:
        item_list[d]= int(c)
for key,value in item_list.items():
    print("{a}{b}".format(a = key, b = value))
