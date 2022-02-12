import socket
import sys

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
        self.port = 1993
        self.server_socket = self.host, self.port
        
    def msg(self):
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn.connect(self.server_socket)
        print(f"\nConnexion etablie avec : {self.host}:{self.port}\n")
        print(f"Tu peux à present communiquer avec {self.host}")
        print("Ecrit ton message ci-dessous")
        
        while True:
            m = input("-> Message $ ")
            data = m.encode("utf8")
            self.conn.sendall(data)
            print("message envoyé")
        
Messenger().msg()