#ceaser cipher with encryption and decryption key 3
from curses.ascii import islower, isupper


def en(s,key):
    st=""
    for i in s:
        char=i
        if(islower(char)):
            temp=(ord(char)+key-97)%26+97
            st+=chr(temp)
        elif(isupper(char)):
            temp=(ord(char)+key-65)%26+65
            st+=chr(temp)
        else:
            temp=(ord(char)+key-32)%96+32
            st+=chr(temp)
    
    print(st)
    return st

def de(s1,key):
    st=""
    for i in s1:
        char=i
        if(islower(char)):
            temp=(ord(char)-key-97)%26+97
            st+=chr(temp)
        elif(isupper(char)):
            temp=(ord(char)-key-65)%26+65
            st+=chr(temp)
        else:
            temp=(ord(char)-key-32)%96+32
            st+=chr(temp)
    print(st)
    pass

p="mA:dhu"
k=en(p,3)
de(k,3)