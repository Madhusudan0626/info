#railfence cipher using python with a height 3 with encryption and decryption
from array import*
import string

s='madhu'
h=3

def en(s,h):
    a=[['\t' for j in range(len(s))] for i in range(h)]

    flag=0
    x=0
    for i in range(len(s)):
        
        if(x==h-1):
            flag=1
        if(x==0):
            flag=0

        if(flag==1):
            a[x][i]=s[i]
            x=x-1
        else:
            a[x][i]=s[i]
            x=x+1
    m=''
    for i in range(h):
        for j in range(len(s)):
            if(a[i][j]!='\t'):
                m+=a[i][j]


    print(a)
    print(m)

def dr(e,h):
    s=""
    a=[['\t' for i in range(len(e))]for i in range(h)]
    flag=0
    l=len(e)
    x=0
    for i in range(len(e)):
        if(x==h-1):
            flag=1
        if(x==0):
            flag=0

        if(flag==1):
            a[x][i]='0'
            x=x-1
        else:
            a[x][i]='0'
            x=x+1
    b=0
    for i in range(h):
        for j in range(len(e)):
            if(a[i][j]=='0'):
                a[i][j]=e[b]
                b=b+1
    st=""
    x=0
    flag=0
    for i in range(len(e)):
        if(x==h-1):
            flag=1
        if(x==0):
            flag=0

        if(flag==1):
            st+=a[x][i]
            x=x-1
        else:
            st+=a[x][i]
            x=x+1
    print(st)
e="muahd"
dr(e,h)
# print(char)