import socket

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
print("Device Name: " + hostname)
print("Device's IP: " + ip)
