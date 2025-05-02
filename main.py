#python port scanner
import socket
from concurrent.futures import ThreadPoolExecutor, as_completed

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

PORT_SERVICES = { #port service dictionary
    22: "SSH",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    443: "HTTPS"
}
def scan_port(host, port):
    """ Attempt to connect to a port on a given IP """
    try: #exception handling(requirement 4)
        with sock:
            sock.settimeout(0.1) #timeout after 100ms (requirement 3)
            result = sock.connect_ex((host, port))
            service = PORT_SERVICES.get(port, "Unknown")
            if result == 0:
                 #returns open ports(requirement 5)
                print(f"[+] Port {port} ({service}) = Open")
            else:
                print(f"[-] Port {port} ({service}) = Closed")
    except Exception as e:
        print(f"[!] Failed to scan port {port} = Closed")

def scan_ports(host, ports):
    """ Scan multiple ports concurrently """
    print(f"Scanning {host} on {len(ports)} ports...")
    
    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in ports:
            executor.submit(scan_port, host, port)
        
if __name__ == "__main__":
    #User Input IP Address(requirement 1)
    host = input("Enter the IP address to scan (e.g., 127.0.0.1): ")
    ports = [22, 25, 53, 80, 443] #ports to scan (requirement 2)
    scan_ports(host, ports)
    