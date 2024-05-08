# write a Java/C/C++/Python program to perform encryption and decryption using the method of 
# Transposition technique. 



from pycipher import caesar

def caesar_encrypt(plaintext,key):
    c=caesar.Caesar(key)
    ciphertext=c.encipher(plaintext)
    return ciphertext

def caesar_decrypt(ciphertext,key):
    c=caesar.Caesar(key)
    plaintext=c.decipher(ciphertext)
    return plaintext

plaintext=input()

key=int(input())

ciphertext = caesar_encrypt(plaintext, key)
decrypted_plaintext = caesar_decrypt(ciphertext, key)

print('Plaintext: ', plaintext)
print('Ciphertext:', ciphertext)
print('Decrypted plaintext:', decrypted_plaintext)
