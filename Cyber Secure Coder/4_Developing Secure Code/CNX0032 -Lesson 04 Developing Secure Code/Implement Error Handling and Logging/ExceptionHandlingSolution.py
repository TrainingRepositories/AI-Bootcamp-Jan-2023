"""
Exception handing proposed solution
Python 3.8.x Solution

Open, read and Hash the contents of a file

Function: HashFile()
Input:    FilePath to Hash
Input:    HashMethod (either SHA256 or SHA512)
return:   True, Hash Digest
          or
          False, "Error Message"
"""

import os  # Standard Python Library Operating System Methods
import hashlib  # Standard Python Hashing Library


def HashFile(filePath, hashMethod="SHA512"):

    # Issue One : Validate the specified hashMethod.
    if hashMethod == "SHA256":
        hashObj = hashlib.sha256(str(filePath).encode('utf-8'))
    elif hashMethod == "SHA512":
        hashObj = hashlib.sha512(str(filePath).encode('utf-8'))

        # Issue Two : Verify the path exists.
        if os.path.exists(filePath):

            # Issue Three: Verify the path is a file (not directory or link).
            if os.path.isfile(filePath):

                # Issue Four: Verify the current user has read access.

                if os.access(filePath, os.R_OK):
                    # Issue Five: The file still may be locked by the OS.
                    #             Use try except to catch these issues.

                    try:
                        # Attempt to open the file.
                        with open(filePath) as fileHandle:

                            # Issue 6: File may be too large to handle.
                            #          Use reasonably sized chunks to read.
                            CHUNK_SIZE = 1024

                            while True:
                                chunk = fileHandle.read(CHUNK_SIZE)
                                if chunk:
                                    hashObj.update((chunk).encode('utf-8'))
                                else:
                                    break
                            hexDigest = hashObj.hexdigest().upper()

                        return True, hexDigest

                    except Exception as msg:
                        return False, "Error: FilePath: " + filePath + "," + str(msg)

                else:
                    return False, "Error: FilePath: " + filePath + " is not readable"

            else:
                return False, "Error: FilePath: " + filePath + " is not a file"

        else:
            return False, "Error: FilePath: " + filePath + " Does not exist"
    else:
        return False, "Invalid Hash Type Specified"


def main():
    print("Hash File Contents")

    # Test Code

    testCases = [
        ["goodfile.txt", "SHA512"],
        ["goodfile.txt", "BADMETHOD"],
        ["missingfile.txt", "SHA512"],
        ["lockedfile.txt", "SHA512"],
        ["directory", "SHA512"]
    ]

    for eachFile in testCases:
        result, msg = HashFile(eachFile[0], eachFile[1])
        if result:
            print("Success: " + msg)
        else:
            print("Failed: " + msg)


if __name__ == '__main__':
    main()
