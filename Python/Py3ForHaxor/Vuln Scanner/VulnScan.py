import PortScanner

target_ip = input("[+] Enter Target to scan for vuln scan: ")
port_number = int(input("[+] Enter Number of ports to scan: "))
vul_file = input("[+] Enter path to vuln list: ")
print("\n")

targets = PortScanner.PortScan(target_ip,port_number) 
targets.scan()

with open(vul_file,'r') as file:
    count=0
    for i in targets.banners:
        file.seek(0)
        for line in file.readlines():
            if line.strip() in i:
                print("[!!] VULNERABLE BANNER: ",i,"ON PORT: ",str(targets.open_ports[count]))
        count+=1