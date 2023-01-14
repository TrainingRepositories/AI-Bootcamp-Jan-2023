"""
Logging
Python 3.8.x

Utilizing the ExceptionHandlingSolution:
    - Open, read and Hash the contents of a file
    - Create a logfile with a unique name based on current date/time
    - Add Detailed Logging of all operations using the
      Python standard logging Library
    - Add test cases to prove the log is generated correctly
"""

import os  # Standard Python Library Operating System Methods
import hashlib  # Standard Python Hashing Library
import logging  # Standard Python Logging Library
import time  # Standard Python Time Module

"""
Implement logging operations as a Class/Object
"""


class Logger:
    def __init__(self, logName):
        try:
            # Turn on Logging
            logging.basicConfig(
                filename=logName,
                level=logging.DEBUG,
                format='%(asctime)s %(levelname)s %(message)s')
        except:
            print("Log Initialization Failure ... Aborting")
            exit(0)

    def writeLog(self, logMessage, logType="INFO"):

        try:
            if logType == "INFO":
                logging.info(logMessage)
            elif logType == "ERROR":
                logging.error(logMessage)
            elif logType == "WARNING":
                logging.warning(logMessage)
            else:
                logging.error(logMessage)

        except Exception as msg:
            logging.error("Invalid Error: " + str(msg))

        return

    def __del__(self):
        logging.info("Logging Shutdown")
        logging.shutdown()


'''
Function: HashFile()
Input:    FilePath to Hash
Input:    Log Object
Input:    HashMethod (either SHA256 or SHA512)
return:   True, Hash Digest
          or 
          False, "Error Message" 
'''


def HashFile(log, filePath, hashMethod="SHA256"):
    msg = "Hashing: " + filePath + " Method: " + hashMethod
    log.writeLog(msg, "INFO", )

    # Issue One : Validate the specified hashMethod.
    if hashMethod == "SHA256":
        hashObj = hashlib.sha256(str(filePath).encode('utf-8'))
    elif hashMethod == "SHA512":
        hashObj = hashlib.sha512(str(filePath).encode('utf-8'))

        # Issue Two : Verify the path exists.
        if os.path.exists(filePath):
            log.writeLog("     Path Exists", "INFO")

            # Issue Three: Verify the path is a file (not directory or link).
            if os.path.isfile(filePath):
                log.writeLog("     Path Is a File", "INFO")

                # Issue Four: Verify the current user has read access.

                if os.access(filePath, os.R_OK):
                    # Issue Five: The file still may be locked by the OS.
                    #             Use try except to catch these issues.
                    log.writeLog("     Path is Accessible", "INFO")

                    try:
                        # Attempt to open the file.
                        with open(filePath) as fileHandle:

                            # Issue 6: File may be too large to handle.
                            #          Use reasonably sized chunks to read.
                            log.writeLog("     Path Opened", "INFO")
                            fileSize = os.path.getsize(filePath)
                            log.writeLog("     File Size: " + str(fileSize), "INFO")

                            CHUNK_SIZE = 1024

                            while True:
                                chunk = fileHandle.read(CHUNK_SIZE)
                                if chunk:
                                    hashObj.update((chunk).encode('utf-8'))
                                else:
                                    break
                            hexDigest = hashObj.hexdigest().upper()
                            log.writeLog("     File Hash: " + hexDigest.upper(), "INFO")

                        return True, hexDigest

                    except Exception as msg:
                        log.writeLog("     " + str(msg), "ERROR")
                        return False, "Error: FilePath: " + filePath + "," + str(msg)

                else:
                    log.writeLog("      Path is Not Readable", "ERROR")
                    return False, "Error: FilePath: " + filePath + " is not readable"

            else:
                log.writeLog("     Path is not a file", "ERROR")
                return False, "Error: FilePath: " + filePath + " is not a file"

        else:
            log.writeLog("      Path does not exist", "ERROR")
            return False, "Error: FilePath: " + filePath + " Does not exist"
    else:
        log.writeLog("      Invalid Hash Type Specified", "ERROR")
        return False, "Invalid Hash Type Specified"


def main():
    print("Hash File Contents")
    # Create a Unique LogFile Name
    path = os.getcwd()
    logName = os.path.join(path, (time.strftime("%Y-%m-%d-%H%M") + "-Log") + ".txt")

    # Create a logger Object
    logObj = Logger(logName)

    # Write Log Heading
    logObj.writeLog("Starting Hashing Test", "INFO")
    logObj.writeLog("=====================", "INFO")
    logObj.writeLog("", "INFO")

    # Test Code

    testCases = [
        ["goodfile.txt", "SHA512"],
        ["goodfile.txt", "BADMETHOD"],
        ["missingfile.txt", "SHA512"],
        ["lockedfile.txt", "SHA512"],
        ["directory", "SHA512"]
    ]

    for eachFile in testCases:
        result, msg = HashFile(logObj, eachFile[0], eachFile[1])
        if result:
            print("Success: " + str(msg))
        else:
            print("Failed: " + str(msg))


if __name__ == '__main__':
    main()
