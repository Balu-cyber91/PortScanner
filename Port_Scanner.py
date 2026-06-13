import socket #socket is for network connections
import threading #threading is for multithreading
from queue import Queue #queue is for multithreading
import sys #sys is for system arguments
import subprocess #subprocess is for running commands
import platform #platform is for checking the operating system

target=""
filename = ""
save_file = False

print(f"""
 /$$$$$$$   /$$$$$$  /$$$$$$$  /$$$$$$$$        /$$$$$$   /$$$$$$   /$$$$$$  /$$   /$$ /$$   /$$ /$$$$$$$$ /$$$$$$$ 
| $$__  $$ /$$__  $$| $$__  $$|__  $$__/       /$$__  $$ /$$__  $$ /$$__  $$| $$$ | $$| $$$ | $$| $$_____/| $$__  $$
| $$  \ $$| $$  \ $$| $$  \ $$   | $$         | $$  \__/| $$  \__/| $$  \ $$| $$$$| $$| $$$$| $$| $$      | $$  \ $$
| $$$$$$$/| $$  | $$| $$$$$$$/   | $$         |  $$$$$$ | $$      | $$$$$$$$| $$ $$ $$| $$ $$ $$| $$$$$   | $$$$$$$/
| $$____/ | $$  | $$| $$__  $$   | $$          \____  $$| $$      | $$__  $$| $$  $$$$| $$  $$$$| $$__/   | $$__  $$
| $$      | $$  | $$| $$  \ $$   | $$          /$$  \ $$| $$    $$| $$  | $$| $\   $$$| $\   $$$| $$      | $$  \ $$
| $$      |  $$$$$$/| $$  | $$   | $$         |  $$$$$$/|  $$$$$$/| $$  | $$| $$ \  $$| $$ \  $$| $$$$$$$$| $$  | $$
|__/       \______/ |__/  |__/   |__/          \______/  \______/ |__/  |__/|__/  \__/|__/  \__/|________/|__/  |__/
""")
print("-"*120)

try:
    if "-o" in sys.argv:
        save_file = True
        try:
            filename = sys.argv[sys.argv.index("-o")+1] #getting the filename from the command line argument
        except IndexError:
            print("Error provide a filename after -o")
            sys.exit()
    for arg in sys.argv[1:]:
        if arg == "-h": #checking if the help flag is provided
            print("Usage: python Port_Scanner.py <target> [-o <filename>]")
            sys.exit()
        elif arg != "-o" and arg !=filename: #checking if the argument is not -o and not the filename
            target=arg 
            break
        else:
            continue
    if not target:
        target=input("Enter the host/IP to scan: ")
    target_ip = socket.gethostbyname(target)
    platform_flag = "-n" if platform.system().lower() == "windows" else "-c" #to check the operating system and set the flag accordingly
    if subprocess.run(["ping", platform_flag, "1", target_ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode != 0:
        # stdout=subprocess.DEVNULL is not to print the output of the command
        # stderr=subprocess.DEVNULL is not to print the error of the command
        # returncode != 0 means the command failed
        print("Host is down")
        sys.exit()
    print(f"Scanning Target: {target_ip}")
    print("-" * 50)
    if save_file:
        with open(filename, "a") as f:
            f.write(f"\n-------Target: {target_ip}-------\n")
except socket.gaierror:
    print("Hostname could not be resolved")
    sys.exit()
except KeyboardInterrupt:
    print("\nExiting the scan")
    sys.exit()

queue = Queue()

def port_scan(port):
    try:
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        if s.connect_ex((target_ip,port)) == 0:
            try:
                service = socket.getservbyport(port, 'tcp') #get the service name for the port
            except:
                service = 'Unknown' #if the service name is not found, print Unknown
            print(f"Port {port:5} is open | Service: {service}")
            #The syntax is {variable:width}.
            #port: The variable you want to print.
            #:: The separator that tells Python "formatting instructions are coming next."
            #5: The number of spaces to reserve.

            #appending results on file
            if save_file:
                with open(filename, "a") as f:
                    f.write(f"Port {port:5} is open | Service: {service}\n")
        s.close()
    except KeyboardInterrupt:
        print("\nExiting the scan")
        sys.exit()
    except:
        pass


def worker():
    while not queue.empty(): #while the queue is not empty
        port = queue.get() #get the port from the queue
        try:
            port_scan(port) #scan the port
        finally:
            queue.task_done() #mark the task as done

for port in range(1,1025):
    queue.put(port)

try:
    for _ in range(100):
        t = threading.Thread(target=worker, daemon=True)
        t.start()

    queue.join()
except KeyboardInterrupt:
    print("\nExiting the scan")
    sys.exit()
except:
    pass #pass is used to do nothing

print("-" * 30 + "\nScan completed")