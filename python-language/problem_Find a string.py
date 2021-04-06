def count_substring(string, sub_string):
    a=len(sub_string)
    cont=0
    for i in range(len(string)-a+1):
        if(string[i:i+a]==sub_string[:]):
            cont+=1
            
    return cont

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
