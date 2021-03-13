if __name__ == '__main__':
    n = int(input())
    arr =[int(i) for i in input().split()]
    arr.sort()
    res = [] 
    for i in arr:
        if i not in res:
            res.append(i)
    a=len(res)
    print(res[a-2])
