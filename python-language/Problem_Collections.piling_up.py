for t in range(int(input())):
    n=int(input())
    lst = list(map(int, input().split()))
    i = 0
    while i < n - 1 and lst[i] >= lst[i+1]:
        i += 1
    while i < n - 1 and lst[i] <= lst[i+1]:
        i += 1
    if i == n - 1 :
        print ("Yes") 
    else :
        print("No")    
