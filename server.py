import socket
import sys
import random
# import time

# import password

if sys.version_info[0] < 3:
    print("""
          CE MODDULE REQUIERT PYTHON 3.X.X
          """
          )
    sys.exit()
 
class Messenger:    
    def __init__(self):
        self.host = socket.gethostbyname(socket.gethostname())
        self.ports = [9000, 5520, 8888, 4512, 55512, 1992, 1993, 1999, 6655, 2031]
        self.port = 1993 #random.choice(self.ports)
        self.server_socket = self.host, self.port
        
    def msg(self):
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn.bind(self.server_socket)
        self.conn.listen(2)
        print(f"\nsocket ouvert: {self.host}:{self.port}\nserver demarré...")
            
        while True:
            client_socket, client_addr = self.conn.accept()
            print(f"[+] {client_addr[0]}:{client_addr[1]} est connecté")
            
            while client_socket:
                s = client_socket.recv(1024)
                data = s.decode("utf-8")
                if data in ['0', 'ok']:
                    break
                else:
                    print(data)

Messenger().msg()