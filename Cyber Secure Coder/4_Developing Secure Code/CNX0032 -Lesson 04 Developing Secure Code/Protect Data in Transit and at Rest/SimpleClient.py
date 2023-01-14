'''
Simple Client Data Transfer in The Clear

In this example, a connection is made between a client
and a simple server running on the same machine over a 
pre-defined and agreed-upon port.

This client application will transfer a text file to the server,
and the server will simply display the contents of the file as it is 
receiving it.

The objective is to run setup and execute wireshark or similiar network 
capture application and capture and view the plaintext data.


'''

import socket           # Import Python Standard Socket Library
import os               # Python Standard Library Operating System Library

from pip._vendor.distlib.compat import raw_input

print("Client Application")
print("Establish a connection to a server")
print("Available on the same host using PORT 5555")

PORT = 5555             # Port Number of Server
CHUNK_SIZE  = 1024      # Size of each chunk to read and send

# Function to Validate the Filename

def ValidateFile(theFile):
    
    # Validate file specification
    
    if os.path.exists(theFile):
        if os.path.isfile(theFile):
            if os.access(fileName, os.R_OK):
                return True
        else:
            return False
    else:
        return False
    

# Simple Client Transfer Class
# Constructor establishes connection
# send transfers buffer to server

class ClientTransfer:
    
    def __init__(self, port):
        
        self.status = False
    
        try:
            # Create a Socket
            self.clientSocket = socket.socket()
            
            # Get my local host address
            localHost = socket.gethostname()
            
            # Specify a local Server Port to attempt a connection
            localPort = port
            
            # Attempt a connection to my localHost and localPort
            self.clientSocket.connect((localHost, localPort))
            
            self.status = "OK"
            
        except Exception as msg:
            self.status = str(msg)
            
    def send(self, buffer):
        
        if self.status == "OK":
            try:
                # Sending message if there was a connection
                self.clientSocket.sendall(buffer)
            except Exception as err:
                # Transfer Failed
                self.status = str(err)
    
    def stop(self):
        self.clientSocket.close()
            
# Main Program Starts Here
#===================================

if __name__ == '__main__':
    
    fileName   = raw_input("Enter filename to transfer: ")
    
    if ValidateFile(fileName):
        
        print("\nAttempting to Connect to Local Server at Port: ", PORT)
        
        clientObj = ClientTransfer(PORT)
        if clientObj.status == "OK":  
            print("Socket Connected ...")
            print("\nOpening file: ", fileName)

            try: 
                with open(fileName, 'rb') as inFile:
                    while True:
                        buffer = inFile.read(CHUNK_SIZE)
                        if buffer:
                            # Send next file chunk
                            clientObj.send(buffer)
                            if clientObj.status == "OK":
                                continue
                            else:
                                # Transfer Failed
                                print('Transfer Failed: ', str(clientObj.status))
                                clientObj.stop()
                                quit()  
                        else:   
                            # Tranfer Completed
                            clientObj.stop()
                            break
                    print('File Transfer sent successfully')
            
            except Exception as err:
                print("File Processing Error: ", str(err))
                clientObj.stop()
                quit()
        else:
            print("\nConnection Failed: ", clientObj.status)
