import socket
import subprocess
import sys
from datetime import datetime

class Scanner(object):
    def __init__(self, host):
        self.server = host
        #Translate a host name to IPv4 address format
        self.RSIP = socket.gethostbyname(self.server)
    def scan(self):
        try:
            for port in range(1,1025):
                #Creates an IPv4(AF_INET) stream socket for TCP(SOCK_STREAM) type connections
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = s.connect_ex((self.RSIP, port))
                if result == 0:
                    print("Port {}: 	 Open").format(port)
                s.close()
        #Cancel Scan
        #make it if cancel button is clicked
        except KeyboardInterrupt:
            sys.exit()

        except socket.gaierror:
            print('Hostname could not be resolved. Exiting')
            sys.exit()
        except socket.error:
            print ("Couldn't connect to server")
            sys.exit()