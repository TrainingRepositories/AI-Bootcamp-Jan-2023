import socket  # network interface library used for raw sockets

hostname = socket.gethostname()
host = socket.gethostbyname(hostname)
s = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_IP)
s.bind((host,0))
s.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1)
s.ioctl(socket.SIO_RCVALL,socket.RCVALL_ON)

print("Network      : Promiscuous Mode")
print("Sniffer      : Ready:")

while True:
    print(s.recvfrom(65565))

