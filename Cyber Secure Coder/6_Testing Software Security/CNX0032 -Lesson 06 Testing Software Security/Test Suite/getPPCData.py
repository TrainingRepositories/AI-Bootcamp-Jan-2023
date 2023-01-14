__author__ = 'rich'

import socket
import json

class GetPPCData():

    @classmethod
    def get_toppings(self):
        toppings = list()

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostbyname('localhost')
        port = 8000
        s.connect((host, port))
        data = s.recv(1024)

        message = "toppings"
        s.send(str.encode(message))
        data = s.recv(1024)
        toppingsjson = bytes.decode(data)
        toppings = json.loads(toppingsjson)

        message = "exit"
        s.send(str.encode(message))
        s.close()
        return toppings

    @classmethod
    def get_prices(self):
        prices = {"medium": 0,
                  "large": 0,
                  "x-large": 0,
                  "med-topping": 0,
                  "large-topping": 0,
                  "xl-topping": 0}

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostbyname('localhost')
        port = 8000
        s.connect((host, port))
        data = s.recv(1024)

        message = "prices"
        s.send(str.encode(message))
        data = s.recv(1024)
        pricejson = bytes.decode(data)
        prices = json.loads(pricejson)

        message = "exit"
        s.send(str.encode(message))
        s.close()
        return prices