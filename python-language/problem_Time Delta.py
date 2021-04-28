from datetime import datetime 


a = '%a %d %b %Y %H:%M:%S %z'
for i in range(int(input())):
    print(int(abs((datetime.strptime(input(), a) -datetime.strptime(input(), a)).total_seconds())))
