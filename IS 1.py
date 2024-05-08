# Write a C program that contains a string (char pointer) with a value \Hello 
# World’. The program should AND , OR and XOR each character in this string 
# with 127 and display the result



import ctypes  #It provides C compatible data types, and allows calling functions in 
s = "Hello World"
and_result = ""
or_result = ""
xor_result = ""

for c in s:
    and_result += chr(ord(c) & 127)
    or_result += chr(ord(c) | 127)
    xor_result += chr(ord(c) ^ 127)

print("AND result:", and_result)
print("OR result :", or_result)
print("XOR result:", xor_result )