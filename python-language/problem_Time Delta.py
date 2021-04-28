import datetime 
import calendar 
from datetime import date

def month_string_to_number(string):
    m = {
        'jan': 1,
        'feb': 2,
        'mar': 3,
        'apr':4,
         'may':5,
         'jun':6,
         'jul':7,
         'aug':8,
         'sep':9,
         'oct':10,
         'nov':11,
         'dec':12
        }
    s = string.strip()[:3].lower()

    try:
        out = m[s]
        return out
    except:
        raise ValueError('Not a month')
    
n=int(input())
for i in range(n):
    a=[]
    b=[]
    a=input().split()
    b=input().split()
    a[2]=month_string_to_number(a[2])
    b[2]=month_string_to_number(b[2])
    for i in range(1,len(a)-2):
        a[i]=int(a[i])
        b[i]=int(b[i])
    
    x=datetime.datetime(a[3], a[2], a[1],int(a[4][:2]), int(a[4][3:5]),int(a[4][6:8]))
    y=datetime.datetime(b[3], b[2], b[1],int(b[4][:2]), int(b[4][3:5]),int(b[4][6:8])) 
    v=x-y
    
    if(a[5][0]=='-'):
        tz1=int((a[5][1:3]))*3600 + int((a[5][3:]))*60
    else:
        tz1=-int((a[5][1:3]))*3600 - int((a[5][3:]))*60
    if(b[5][0]=='-'):
        tz2=-int((b[5][1:3]))*3600 - int((b[5][3:]))*60
    else:
        tz2=int((b[5][1:3]))*3600 + int((b[5][3:]))*60
    tz3=tz1-tz2
    
    print(int(v.total_seconds())+tz3)
