import socket
from IPy import IP

def check_ip(ip):                                                                       #User must provide valid IP, not Domain name
    try:
        IP(ip)                                                                          #IP lib func
        return ip
    except ValueError:
        return socket.gethostbyname(ip)                                                 #get ip from domain

def get_banner(s):                                                                      #Service Running
    return s.recv(1024)

def scan_port(ip,port):
    try:
        sock = socket.socket()                                                          #socket script
        sock.settimeout(1)                                                              #set timeout to 1 sec. This effects accuracy of result
        sock.connect(ip,port)
        try:
            banner= get_banner(sock)
            print('[+] Port ',port,' is Open => ',str(banner.decode().strip('\n')))     #Data is in binary,so convert and strip newline chars. 
        except:
            pass
    except:
        #print('[-] Port ',port,' is Closed')
        pass

def scan(ip,p):
    c_ip=check_ip(ip)
    print("\n[=>] Scanning Target: ",ip)
    for port in range(1,p):
        scan_port(c_ip,port)
    return 0

if __name__ == "__main__":                                                              #When this file is imported, we don't want the code below to run.Thus, this would run only if its the main guy, not imported guy.
    targets = input('[+] Enter Target(s) to Scan: <split Multiple Targets with comma (,)>')
    p=int(input("Enter num of ports to scan: "))
    if ',' in targets:                                                                  #To check if they provided multiple targets
        for ip_add in targets.split(","):
            scan(ip_add.strip(" "),p)
    else:
        scan(targets,p)