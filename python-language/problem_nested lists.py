if __name__ == '__main__':
    f1=[]
    def sort(f1):
        f1.sort(key = lambda x: x[1])
        return f1
    for _ in range(int(input())):
        f1.append([input(),float(input())])
    f1=sort(f1)
    for i in range(len(f1)):
        if(f1[0][1]<f1[i][1]):
            t=f1[i][1]
            break;
    name=[]
    for i in range(len(f1)):
        if(t==f1[i][1]):
            name.append(f1[i][0])
    name.sort()
    for i in range(len(name)):
        print(name[i])       
