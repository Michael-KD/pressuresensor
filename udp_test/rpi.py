import socket
import sys
from time import sleep
import random
from struct import pack

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host, port = '169.231.34.145', 65000 # idk which pc ip to use
server_address = (host, port)

# Generate some random start values
x, y, z = random.random(), random.random(), random.random()

# Send a few messages
for i in range(10):

    # Pack three 32-bit floats into message and send
    message = pack('3f', x, y, z)
    sock.sendto(message, server_address)
    print('Sent')

    sleep(1)
    x += 1
    y += 1
    z += 1