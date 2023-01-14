__author__ = 'rich'

import sqlite3
import socket
import json

conn = sqlite3.connect("pizza.db")
cursor = conn.cursor()

toppings = list()
for row in cursor.execute("SELECT * FROM toppings ORDER BY topping"):
   toppings.append(row[0])

toppingslist = str.encode(json.dumps(toppings))
prices = {'medium':0,
          'large':0,
          'x-large':0,
          'med-topping':0,
          'large-topping':0,
          'xl-topping':0}

for row in cursor.execute("SELECT * FROM prices"):
   prices[row[0]] = row[1]

priceslist = str.encode(json.dumps(prices))
conn.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ""
port = 8000
server.bind((host, port))
server.listen(5)

while True:
   print("Listening for a client...")
   client, addr=server.accept()
   print("Accepted connection from:", addr)
   client.send(str.encode('Welcome to my server!'))

   while True:
      data = client.recv(1024)
      command = bytes.decode(data)
      if (command == 'toppings'):
         print("   Sending toppings list")
         client.send(toppingslist)
      elif (command == 'prices'):
         print("   Sending price list")
         client.send(priceslist)
      elif (command == 'exit'):
         print("   Disconnecting client")
         break
      else:
         print("Received:",command)
         client.send(str.encode("Invalid command"))

   client.close()