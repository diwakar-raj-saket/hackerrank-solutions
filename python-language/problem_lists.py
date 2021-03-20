if __name__ == '__main__':
    N = int(input())
    lit=[]
    for i in range(N):
        a=input().strip().split(' ')
        if(a[0]=="append"):
            lit.append(int(a[1]))
        elif(a[0]=="insert"):
            lit.insert(int(a[1]),int(a[2]))
        elif(a[0]=="remove"):
            lit.remove(int(a[1]))
        elif(a[0]=="pop"):
            lit.pop()
        elif(a[0]=="sort"):
            lit.sort()
        elif(a[0]=="reverse"):
            lit.reverse()
        elif(a[0]=="print"):
            print(lit)
        
