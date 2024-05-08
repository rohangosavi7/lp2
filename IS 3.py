# To implement a Simplified Data Encryption Standard (S-DES) algorithm. 

!pip install DES


from des import DesKey
key = DesKey(b"secret_k") # Define the key to be used (64 bits or 8 bytes)
plaintext = input("Enter plaintext: ").encode() # Prompt the user to enter plaintext
ciphertext = key.encrypt(plaintext, padding=True) # Encrypt the plaintext using DES
print("Ciphertext:", ciphertext.hex()) # Print the ciphertext
decrypted_plaintext = key.decrypt(ciphertext, padding=True) # Decrypt the ciphertext using 
print("Decrypted plaintext:", decrypted_plaintext.decode()) # Print the decrypted plaintex