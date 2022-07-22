import caesar
import atbash

e = 'e'
d = 'd'
c = 'c'
a = 'a'

numeric_key = int(input('enter numeric key'))
plaintext = input('enter plaintext')
cipher = input('chose a cipher')
encryption = input('chose a encryption')

if cipher == c:
    if encryption == e:
        print(caesar.encode(plaintext, numeric_key))
    elif encryption == d:
        print(caesar.decode(plaintext, numeric_key))
        
if cipher == a:
    if encryption == e:
        print(atbash.encode(plaintext))
    elif encryption == d:
        print(atbash.decode(plaintext))
              
              


    