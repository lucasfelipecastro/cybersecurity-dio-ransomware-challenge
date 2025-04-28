# Python Ransomware

A simple implementation of ransomware using Python that encrypts and decrypts files using AES encryption in CTR mode. This project demonstrates the process of encrypting a file and saving it with a custom extension, and then decrypting it back to its original form.

## Features

- Encrypts files with AES encryption (CTR mode).
- Decrypts previously encrypted files using the same key.
- A simple, illustrative example of ransomware behavior (for educational purposes only).

## Installation

Make sure you have Python installed on your system. You will also need the `pyaes` library for AES encryption. You can install it using pip:

```bash
pip install pyaes
```

## Usage
There are two main components in this project: the Encrypter and the Descripter.

### Encrypter
The Encrypter encrypts a given file using a predefined key. The file is then saved with a .ransomwaretroll extension.
```bash
python encrypter.py
```

### Descripter
The Descripter decrypts a file that was encrypted by the Encrypter. The decrypted file is saved with the original file name.
```bash
python descripter.py
```

## Example:

  Encrypting a file: Run the Encrypter script to encrypt sample.txt. This will create sample.txt.ransomwaretroll.
  Decrypting the file: Run the Descripter script to decrypt sample.txt.ransomwaretroll back into sample.txt.

## Notes

  - This is a simple, educational demonstration of a ransomware-like encryption and decryption process.
  - The encryption key must be kept secure, as it is needed to decrypt the files.
  - This code is not intended for malicious use. Please use it responsibly and only for educational purposes.

Disclaimer
This code is intended for educational purposes only. Do not use this in any unauthorized or harmful manner. The purpose is to demonstrate how ransomware-like behavior can be implemented using Python for educational and research purposes.
