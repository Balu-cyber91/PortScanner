#utlizing the threading and queue module to scan multiple ports at once

import socket
import sys
import threading
from queue import Queue

try:
    target = input("Enter the host/IP to scan: ")
    target_ip = socket.gethostbyname(target)
    queue = Queue()
    print(f"Scanning Target: {target_ip}")
    print("-" * 50)
except socket.gaierror: #gaierror is getaddrinfo error
    print("Hostname could not be resolved")
    sys.exit()


#function to scan the ports
def port_scan(port):
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    if s.connect_ex((target_ip,port))==0:
        print(f"Port {port} is open")
    s.close()

#worker function to scan the ports
def worker():
    while True:
        port = queue.get()
        port_scan(port)
        queue.task_done()

#adding ports to the queue
for port in range(1,1025):
    queue.put(port)

#creating 100 threads to scan the ports
for _ in range(100):
    t = threading.Thread(target=worker, daemon=True)
    t.start()

queue.join()
print("Scan completed")
