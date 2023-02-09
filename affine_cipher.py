from curses.ascii import isalnum, islower
from operator import mod
from statistics import multimode


def encrypter(s,a,b):#s is the planetext || a and b the encryotion key
    s1=''
    # print(s1)
    s2=''
    for i in s:    

        temp=i
        t=ord(temp)
        t=t-32
        t=(a*t+b)%95
        t+=32
        temp=chr(t)
        s2+=temp
    print('Encrypted text : ',s2)
    return s2

def decrypter(s,a,b):
    mi=moduloInverse(a)
    print(mi)
    s1=''
    for i in s:
        temp=i
        t=ord(temp)
        t=t-32
        t=mi*(t-b)%95
        t=t+32
        temp=chr(t)
        s1+=temp
    print('Decrypted Text is : ',s1)

def moduloInverse(a):
    i=1
    for i in range(95):
        if(a*i)%95==1:
            return i
        else:
            return 0 
#__main__
s=input('Enter the string\n')
print('Original Text : ',s)
en=encrypter(s,4,6)
decrypter(en,4,6)
