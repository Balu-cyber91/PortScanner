import socket
from datetime import datetime

target = input("Enter the host/IP to scan: ")
target_ip = socket.gethostbyname(target) #convert hostname to IP

print("-" * 50)
print("Scanning Target: " + target_ip)
print("Time started: " + str(datetime.now())) #convert datetime to string
print("-" * 50)

try:
    for port in range(1,1025):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create a socket object
        # AF_INET is Address Family for IPv4 and SOCK_STREAM is TCP
        socket.setdefaulttimeout(0.5) #set a timeout for the socket
        result = s.connect_ex((target_ip, port)) #establish a connection to a remote address
        if result == 0:
            print(f"Port {port} : Open")
        s.close()
except KeyboardInterrupt:
    print("\nExiting")