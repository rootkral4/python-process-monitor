import psutil

userMenu = """
[0] = List running processes
[1] = List running processes (Only Using Network)
[2] = List running processes (Only Using Network, DETAILED)
[3] = Get process network information by pid
"""
def GetProcInfoByPID(pid):
    for proc in psutil.net_connections():
        if proc.pid == int(pid):
            rtrnval += [proc.fd, proc.family, proc.type, proc.laddr, proc.raddr, proc.status, proc.pid]
            break
    return rtrnval

def FindNameByPID(pid):
    name = "NULL"
    for proc in psutil.process_iter():
        if proc.pid == int(pid):
            name = proc.name()

    return name

def ListProcesses():
    pCounter = 0
    for proc in psutil.process_iter():
        print("[+] Process Name :", proc.name(), "\n [-] Process Identifier :", proc.pid)
        pCounter += 1
    print(pCounter, "Process Running")

def ListProcessesNetwork():
    pCounter = 0
    for proc in psutil.net_connections():
        print("[+] Process Name :", FindNameByPID(proc.pid), "\n [-] Process Identifier :", proc.pid)
        pCounter += 1
    print(pCounter, "Network Connection Active")

def ListProcessesNetworkDetailed():
    pCounter = 0
    conns = []
    for proc in psutil.net_connections():
        print("[+] Process Name :" + FindNameByPID(proc.pid), 
            "\n [-] Process Identifier :" + str(proc.pid))
        for con in psutil.net_connections():
            if con.pid == proc.pid:
                conns.append(con)
        for c in conns:
            print(" [*] ", str(c))
            pCounter += 1
        conns.clear()
        
    print(pCounter, "Network Connection Active")


while True:
    print(userMenu)
    choice = int(input("->"))
    if choice == 0:
        ListProcesses()
    elif choice == 1:
        ListProcessesNetwork()
    elif choice == 2:
        ListProcessesNetworkDetailed()
    elif choice == 3:
        pid = int(input("Process ID :"))
        print(GetProcInfoByPID(pid))
    else:
        print("Invalid Choice ")
