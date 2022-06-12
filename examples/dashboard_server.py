"""
A basic command-line style interface for interacting with the
UR Dashboard Server

https://www.universal-robots.com/articles/ur/dashboard-server-e-series-port-29999/

"""

import socket
import sys

address = "127.0.0.1"
port = 29999

# initaialze a TCP socket using IPv4
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((address, port))

print(s.recv(1024).decode())

while True:
    command = input(":> ")
    
    if command == "exit":
        sys.exit()

    # Append newline to signal end of message
    command += "\n"

    # convert ascii to bytes
    s.send(command.encode())
    
    # receive bytes (max. 1024)
    data = s.recv(1024)

    if(data):
        print(data.decode())

    




