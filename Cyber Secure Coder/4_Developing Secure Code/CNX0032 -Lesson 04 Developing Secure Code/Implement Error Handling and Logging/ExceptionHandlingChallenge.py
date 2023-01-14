import hashlib  # Python Standard Hashing Library

"""
Open, read and hash the contents of a file

Function: HashFile()
Input:    FilePath to Hash
Input:    Hash Method (MD5, SHA256) default is SHA256
result:   Return the Hash Digest

"""


def hashfile(filepath, hashMethod='SHA256'):
    with open(filepath) as fileHandle:

        filecontents = fileHandle.read()

        if hashMethod == 'SHA256':
            hashobj = hashlib.sha256(str(filecontents).encode('utf-8'))
        else:
            hashobj = hashlib.md5(str(filecontents).encode('utf-8'))

        hashobj.update((filecontents).encode('utf-8'))
        hexdigest = hashobj.hexdigest().upper()

        return hexdigest


"""
Main Test Function
"""


def main():
    print("Hashing the File Contents")

    filetohash = "goodfile.txt"
    result = hashfile(filetohash, "MD5")
    print("File: ", filetohash, " Hash: ", result)


if __name__ == '__main__':
    main()
