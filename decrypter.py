import os
import pyaes

# Open the encrypted file
encrypted_file_name = "sample.txt.ransomwaretroll"
with open(encrypted_file_name, "rb") as file:
    encrypted_data = file.read()

# Decryption key
decryption_key = b"newdecryptionkey"
aes = pyaes.AESModeOfOperationCTR(decryption_key)
decrypted_data = aes.decrypt(encrypted_data)

# Remove the encrypted file
os.remove(encrypted_file_name)

# Create the decrypted file
decrypted_file_name = "sample.txt"
with open(decrypted_file_name, "wb") as new_file:
    new_file.write(decrypted_data)
