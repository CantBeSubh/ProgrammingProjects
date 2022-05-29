import socket
from IPy import IP

class PortScan():
    target=("")
    port=int(0)
    banners=[]
    open_ports=[]
    def  __init__(self,t,p):
        self.target=t
        self.port=p
        
    def check_ip(self):                                                                     
        try:
            IP(self.target)                                                                          
            return self.target
        except ValueError:
            return socket.gethostbyname(self.target)                                                 

    def scan_port(self,port):
        try:
            converted_ip=self.check_ip()
            sock = socket.socket()
            sock.settimeout(1)                                                            
            sock.connect(converted_ip,port)
            self.open_ports.append(port)
            try:
                banner= sock.recv(1024).decode().strip('\n')
                self.banners.append(banner)    
            except:
                self.banners.append(" ")    
        except:
            #print('[-] Port ',port,' is Closed')
            pass
        sock.close()

    def scan(self):
        for port in range(1,self.port):
            self.scan_port(port)