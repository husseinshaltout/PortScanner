import socket
import subprocess
import sys
from datetime import datetime

class Scanner(object):
    def __init__(self, host, PRfrom, PRto):
        self.server = host
        self.PRfrom = PRfrom
        self.PRto = PRto
        #Translate a host name to IPv4 address format
        self.RSIP = socket.gethostbyname(self.server)
    def scan(self):
        print(self.server)
        print(self.RSIP)
        self.Tstart = datetime.now()
        self.rd = {}
        try:
            for port in range(int(self.PRfrom), int(self.PRto)):
                #Creates an IPv4(AF_INET) stream socket for TCP(SOCK_STREAM) type connections
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = s.connect_ex((self.RSIP, port))
                print("Port: ",port)
                if result == 0:
                    print(port,": open")
                    self.rd[port] = "Open"
                else:
                    print(result)
                    self.rd[port] = "Closed"
                s.close()
            print(self.rd)
        #Cancel Scan
        except KeyboardInterrupt:
            print("canceled")
            sys.exit()

        except socket.gaierror:
            print('Hostname could not be resolved. Exiting')
            sys.exit()
        except socket.error:
            print ("Couldn't connect to server")
            sys.exit()
        self.Tend = datetime.now()
        self.totaltime = self.Tend - self.Tstart
        return self.totaltime, self.rd
    def start(self):
        self.scan()
if __name__ == "__main__":
    Scanner = Scanner('www.google.com',80,81)        
    Scanner.start()