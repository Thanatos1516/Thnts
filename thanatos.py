import socket

#Default ports for scanning
DEFAULT_PORTS = [21, 22, 23, 80, 443, 445, 3389]

def scan_port(ip, port):
    #Checking a single host
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  #1 second  time delay
    result = sock.connect_ex((ip, port))
    sock.close()
    return port if result == 0 else None

def get_user_input():
    #Reception IP address and ports from user
    ip = input("Enter the IP address: (For Example: 127.0.0.1): ").strip()
    if not ip:
        ip = "127.0.0.1"  # Default IP, if user input nothing
    
    ports_input = input("Input ports:  (For example: 20-100 OR 80,443) or input nothing for default ports: ").strip()
    
    if not ports_input:
        return ip, DEFAULT_PORTS
    
    # If the range is specified (For example:  20-100)
    if "-" in ports_input:
        try:
            start, end = map(int, ports_input.split("-"))
            return ip, list(range(start, end + 1))
        except ValueError:
            print("Wrong range! The program will use default ports..")
            return ip, DEFAULT_PORTS
    
    # If individual ports are specified (For example: 80,443)
    try:
        ports = [int(p) for p in ports_input.split(",")]
        return ip, ports
    except ValueError:
        print("Wrong format: The program will use default ports..")
        return ip, DEFAULT_PORTS

def port_scanner():
    #Main scan function
    print("Port scanner v1.0")
    ip, ports = get_user_input()
    print(f"Scanning in progress on {ip}, ports: {ports}")
    
    open_ports = []
    for port in ports:
        if scan_port(ip, port):
            open_ports.append(port)
    
    if open_ports:
        print(f"Open ports on {ip}: {open_ports}")
    else:
        print(f"There are no open ports on the {ip}.")

if __name__ == "__main__":
    port_scanner()
