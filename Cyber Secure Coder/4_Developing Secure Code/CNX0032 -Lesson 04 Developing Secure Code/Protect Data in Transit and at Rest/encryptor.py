import pyAesCrypt
from os import stat
from pip._vendor.distlib.compat import raw_input

# encryption/decryption buffer size
bufferSize = 64 * 1024
password = raw_input("Enter the password used to encrypt: ")  # encryption of file data.txt
fileName = raw_input("Enter filename to encrypt: ")
with open(fileName, "rb") as fIn:
    with open("top_secret.txt.aes", "wb") as fOut:
        pyAesCrypt.encryptStream(fIn, fOut, password, bufferSize)  # get encrypted file size
        encFileSize = stat("top_secret.txt.aes").st_size
print(encFileSize)  # prints file size# decryption of file data.aes with open(“data.txt.aes”, “rb”) as fIn:
