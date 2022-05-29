##!/usr/bin/env python3
#now i can ./linux_priv_esc and be the coolest haxor in the hood

#Linux Privilege Escalation Script
#It will...
#   + OS,Release and Kernal Release
#   + Root services dump
#   + SUID-GUID Check
#   + Find SUID/GUID abusible binaries

import os

def OS_KERNEL_CHECK():
    print("[+]OS/Kernal Check Function")
    os.system('uname -a')
    os.system('cat /etc/os-release')

def ROOT_SERVICE_CHECK():
    print("[+]Root Service Check Function")
    os.system('ps aux | grep root')

def SUID_GUID_CHECK():
    print("[+]SUID Check Function")
    os.system('find / -perm -u=s -type f 2 > /dev/null')
    print("\n[+]GUID Check Function")
    os.system('find / -perm -g=s -type f 2 > /dev/null')

#MAIN DRIVER
while(True):
    option = input("""
[+]Please choose:
0. Full Scan
1. Kernal/OS 
2. Root Service
3. SUID/GUID
4. Exit
""")
    #os.system('clear')
    if option=="0":
        OS_KERNEL_CHECK()
        print("-------------------------------------------")
        ROOT_SERVICE_CHECK()
        print("-------------------------------------------")
        SUID_GUID_CHECK()
        print("-------------------------------------------")
        hold=input("FULL SCAN COMPLETE. Press ENTER to return to main menu")
        exit()
    elif option=="1" :
        OS_KERNEL_CHECK()
    elif option=="2" :
        ROOT_SERVICE_CHECK()
    elif option=="3" :
        SUID_GUID_CHECK()
    elif option=="4" :   
        exit()
    else:
        print("\n[!!]Enter Valid option!")
        continue 
    
    hold=input("Press ENTER to return to main menu")