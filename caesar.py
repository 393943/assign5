def encode(plaintext, key):
    encrypted = ""
    for i in plaintext:
        
        if i.isupper():
            i_index = ord(i) - ord('A')
            i_shifted = (i_index + key)%26 + ord('A')
            i_new = chr(i_shifted)
            encrypted += i_new
            
        elif i.islower():
            i_index = ord(i) - ord('a')
            i_shifted = (i_index + key)%26 + ord('a')
            i_new = chr(i_shifted)
            encrypted += i_new
            
        else:
            encrypted += i
            
    return encrypted



def decode(ciphertext, key):
    decrypted = ""
    for i in ciphertext:
        
        if i.isupper():
            i_index = ord(i) - ord('A')
            i_shifted = (i_index - key)%26 + ord('A')
            i_new = chr(i_shifted)
            decrypted += i_new
            
        elif i.islower():
            i_index = ord(i) - ord('a')
            i_shifted = (i_index - key)%26 + ord('a')
            i_new = chr(i_shifted)
            decrypted += i_new
            
        else:
            decrypted += i
        
    return decrypted
        