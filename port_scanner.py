import socket
import sys
from datetime import datetime

def scan_target(target, start_port=1, end_port=1024):
    print(f"\n[*] Starting Scan on Target: {target}")
    print(f"[*] Time started: {datetime.now()}")
    print("-" * 50)
    
    try:
        # Scan range of ports
        for port in range(start_port, end_port + 1):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.5) # Fast timeout
            
            # Returns 0 if connection successful (Port Open)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"[+] Port {port} is OPEN")
            s.close()
            
    except KeyboardInterrupt:
        print("\n[!] Exiting Program.")
        sys.exit()
    except socket.gaierror:
        print("\n[!] Hostname could not be resolved.")
        sys.exit()
    except socket.error:
        print("\n[!] Could not connect to server.")
        sys.exit()
    
    print("-" * 50)
    print(f"[*] Scan completed.")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        target_ip = sys.argv[1]
    else:
        target_ip = input("Enter target IP: ")
    
    scan_target(target_ip, 20, 85)
