# program for caeser chiper information sequirity
from curses.ascii import isalnum, islower, isupper
from sys import flags

def encrypter(otext,shifter):
    result=''
    result1=[]
    for i in range(len(otext)):
      for j in otext[i]:
        char=j
        if islower(char):
          temp=(ord(char)+shifter-97)%26+97
          result+=chr(temp)
        
        elif(isupper(char)):
          temp=(ord(char)+shifter-65)%26+65   
          result+=chr(temp)   
        
        #if(char=='\n' or char==' ' or char=='.' or char==',' or char==':' or char==';' or char=='/' or char=='*' or char=='&' or char=='`' or char=="'" or char=='"' or char=='!' or char=='@'):
        else:
          result+=char
      result1.append(result)
      result=''
    return result1

def decrypter(etext,shifter):
  result=''
  result1=[]
  for i in range(len(etext)):
    for j in etext[i]:
      char=j
      if islower(char):
        temp=(ord(char)-shifter-97)%26
        if temp<0:
          temp+=26
        temp+=97
        result+=chr(temp)

      elif(isupper(char)):
        temp=(ord(char)-shifter-65)%26
        if temp<0:
          temp+=26
        temp+=65
        result+=chr(temp)
      #if(char=='\n' or char==' ' or char=='.' or char==',' or char==':' or char==';' or char=='/' or char=='*' or char=='&' or char=='`' or char=="'" or char=='"' or char=='!' or char=='@'):
      else:  
        result+=char
    result1.append(result)
    result=''
  return result1

def makelist(f):
  m=[]
  while(True):
    line=f.readline()
    if(line==''):
      break
    m.append(line)
  return m
#__main__

while(1):
  print('1.Encrypt')
  print('2.Decrypt')
  print('3.Exit')
  n=int(input('Enter the choice : '))
  if(n==1):
    s=input('Enter a file name : ')
    fl=open(s,'r')

    m=makelist(fl)

    x=int(input('Enter the shift value\n'))
    k=encrypter(m,x)
    print(k)
    s1=input('Enter the file for storing output : ')
    f2=open(s1,'w')
    f2.writelines(k)
    fl.close()
    f2.close()
    
  elif(n==2):
    s1=input('Enter the encrypted file name : ')
    file1=open(s1,'r')

    m1=makelist(file1)
    
    x1=int(input('Enter the shift value\n'))
    m2=decrypter(m1,x1)
    print(m2)
    s2=input('Enter the file for storing output : ')
    file2=open(s2,'w')
    file2.writelines(m2)
    file1.close()
    file2.close()
    
  else:
    print('Please Enter valid choice')
    break

#-------------------------------------------------------------
