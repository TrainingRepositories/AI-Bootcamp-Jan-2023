'''
Simple Server to Receive Data from Client

In this example a connection is made between a client
and simple server running on the same machine over a 
pre-defined and agreed upon port.

This server application will wait for a connection request
over a pre-defined port.

Once a connection is established the server will receive data sent 
over the port and display the contents of the recevied data.

The objective is to run setup and execute wireshark or similiar
network capture application and capture and view the plaintext 
data.

'''

import socket       # import Python Standard Socket Library
import select

PORT = 5555


# Simple Server Class
# Constructor establishes waits for a connection
# from a client over the specified port

class ServerTransfer:
    
    def __init__(self, port):
        
        self.status = False
        self.buffer = ''
        
        try: 
            # Create Socket for listening
            
            serverSocket = socket.socket()
            
            # Get my local host address
            
            localHost = socket.gethostname()
            
            # Specify a local Port to accept connections on
            
            localPort = port
            
            # Bind mySocket to localHost and the specified localPort
            
            serverSocket.bind((localHost, localPort))
            
            # Begin Listening for connections
            
            serverSocket.listen(1)
            
            # Wait for a connection request.
            # Note this is a synchronous call,
            # meaning the program will halt until
            # a connection is received.
            # Once a connection is received,
            # we will accept the connection and obtain the 
            # ipAddress of the connector.
            
            print('\nWaiting for Connection Request')
            
            self.conn, self.client = serverSocket.accept()
            
            # Print a message to indicate we have received a connection
            
            self.status = "OK"
                       
        except Exception as err:
            self.status = str(err)
            
    def recv(self):
        
        if self.status == "OK":
            try:
                # Awaiting data from client
                self.buffer = self.conn.recv(1024)  
            except Exception as err:
                # Transfer Failed
                self.status = str(err)

# Main Program Starts Here
#===================================

if __name__ == '__main__':
    
    print("Server Starting up\n")
    print("Waiting for Connection ...")
    
    serverObj = ServerTransfer(PORT)
    
    if serverObj.status == "OK":
        print("\nConnection Established: ", serverObj.client)
        while True:
            serverObj.recv()
            if serverObj.status == 'OK':
                if serverObj.buffer:
                    print(serverObj.buffer)
                else:
                    print("\n\n=================================\n\n")
                    print("Transfer Completed")
                    break
            else:
                print("\n\nConnection Failed: ", serverObj.status)
                quit()
    else:
        print("\nConnection Failed: ", serverObj.status)

        
    
    
          
    
