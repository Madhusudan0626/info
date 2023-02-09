plaintext="hello i am madhusudan"
plaintext=plaintext.replace(" ","")
key=4#1<key<len(plaintext)

ciphertext=['']*key

for column in range(key):
    pointer = column
    while pointer < len(plaintext):
        ciphertext[column]+=plaintext[pointer]
        
        pointer+=key

print(''.join(ciphertext))