"""
Simple HTTPServer in Python

From the Web Browser on the same machine
http://127.0.0.1:8000/

"""

import http.server
import socketserver
from functools import partial

"""
Request Authorization Parameters
"""
AUTH_CLIENT = "127.0.0.1"
ALLOWED_CHARS = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789?=\'./\r\n\\'"
MAX_REQ_SIZE = 40
DIRECTORY = "web"
PORT = 8000


class MyRequestHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):

        allowed = True
        for eachChar in str(self.raw_requestline, 'utf-8'):
            if eachChar in ALLOWED_CHARS:
                continue
            else:
                allowed = False
                print(ord(eachChar))
                break

        # Check the request length
        if len(self.raw_requestline) < MAX_REQ_SIZE:
            # Check for valid characters in request
            if allowed:
                # Complete client validated client address
                if self.client_address[0] == AUTH_CLIENT:
                    return http.server.SimpleHTTPRequestHandler.do_GET(self)
                else:
                    self.send_error(401, 'Unauthorized Client')
            else:
                self.send_error(400, 'Request contains invalid characters')
        else:
            self.send_error(400, 'Request Length too long')


Handler = MyRequestHandler

# MyHandle = partial(Handler, directory='C:\\web')
# server = socketserver.TCPServer(('0.0.0.0', PORT), MyHandle)

server = socketserver.TCPServer(('0.0.0.0', PORT), Handler)
print("Server Running on TCP " + str(PORT))

server.serve_forever()
