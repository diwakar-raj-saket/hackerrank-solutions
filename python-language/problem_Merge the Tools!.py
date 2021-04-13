import textwrap
def removeDuplicate(str, n): 
    index = 0
    for i in range(0, n): 
          
        for j in range(0, i + 1): 
            if (str[i] == str[j]): 
                break
                   
        if (j == i): 
            str[index] = str[i] 
            index += 1
              
    return "".join(str[:index]) 
  


def merge_the_tools(string, k):
    c=textwrap.wrap(string, k)
    for i in c:
        print(removeDuplicate(list(i), k)) 
    
    

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
