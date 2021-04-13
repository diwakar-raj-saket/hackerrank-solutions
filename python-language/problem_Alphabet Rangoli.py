def print_rangoli(size):
    a=[]
    c=[]
    d=[]
    b=''
    n=2*(2*size-1)-1
    fill='-'
    for i in range(0,size):
        
        b=b+chr(96+size-i)+'-'
        a.append(b[:-1])
        c.append('-'+a[i][::-1])
    c.pop()
    c.insert(0,'')
    for i in range(len(a)):
        d.append(a[i]+c[i])
    for i in range(len(a)):
        temp=d[i]
        print(temp.center(n,fill))
    for i in range(0,len(a)-1):
        temp=d[len(a)-2-i]
        print(temp.center(n,fill))
        
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
