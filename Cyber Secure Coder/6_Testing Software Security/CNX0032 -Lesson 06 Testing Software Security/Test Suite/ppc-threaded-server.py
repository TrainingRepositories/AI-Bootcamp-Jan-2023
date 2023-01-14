__author__ = 'rich'

import socket
import json
import sqlite3
import threading

class clientThread(threading.Thread):
    def __init__(self, client, address):
        threading.Thread.__init__(self)
        self.client = client
        self.addr = address

        conn = sqlite3.connect("pizza.db")
        cursor = conn.cursor()

        toppings = list()
        for row in cursor.execute("SELECT * FROM toppings ORDER BY topping"):
           toppings.append(row[0])
        self.toppingslist = str.encode(json.dumps(toppings))

        prices = {'medium':0,
                  'large':0,
                  'x-large':0,
                  'med-topping':0,
                  'large-topping':0,
                  'xl-topping':0}
        for row in cursor.execute("SELECT * FROM prices"):
           prices[row[0]] = row[1]
        self.priceslist = str.encode(json.dumps(prices))
        conn.close()

    def run(self):
        print("   Sending welcome to ", self.addr)
        self.client.send(str.encode('Welcome to my server!'))
        while True:
           print("   Waiting for command from ", self.addr)
           data = self.client.recv(1024)
           command = bytes.decode(data)
           if (command == 'toppings'):
              print("   Sending toppings list to ", self.addr)
              self.client.send(self.toppingslist)
           elif (command == 'prices'):
              print("   Sending price list to ", self.addr)
              self.client.send(self.priceslist)
           elif (command == 'exit'):
              print("   Disconnecting ", self.addr)
              break
           else:
              print("   Received bad command from ",self.addr)
              self.client.send(str.encode("Invalid command"))
        print("   Closing connection with ", self.addr)
        self.client.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ""
port = 8000
server.bind((host, port))
server.listen(5)

while True:
    print("Listening for a client...")
    client, addr=server.accept()
    print("Accepted connection from:", addr)
    client1 = clientThread(client, addr)
    client1.start()
