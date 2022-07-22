def encode(plaintext):
    encrypted = ''
    
    for i in plaintext:
        if ord(i) < 65:
            encrypted += i
        if 65 <= ord(i) <= 90:
            if i.isupper():
                i_index = ord(i) + 25
                i_shifted = i_index % 90
                encrypted += chr(90 - i_shifted)
                
        if 97 <= ord(i) <= 122:
            if i.islower():
                i_index = ord(i) + 25
                i_shifted = i_index % 122
                encrypted += chr(122- i_shifted)
                
                
    return encrypted

def decode(plaintext):
    decrypted = ''
    
    for i in plaintext:
        if ord(i) < 65:
            decrypted += i
        if 65 <= ord(i) <= 90:
            if i.isupper():
                i_index = ord(i) + 25
                i_shifted = i_index % 90
                decrypted += chr(90 - i_shifted)
                
        if 97 <= ord(i) <= 122:
            if i.islower():
                i_index = ord(i) + 25
                i_shifted = i_index % 122
                decrypted += chr(122- i_shifted)
                
    return decrypted
