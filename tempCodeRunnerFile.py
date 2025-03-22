import socket
import pyfiglet

print("_" * 60)
ascii_art = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_art)
print("_" * 60)

#Aatif Maharjan
def scan_port(target, port):
    """Checks if a port is open on the target IP."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)  # Timeout to avoid long waits
    if s.connect_ex((target, port)) == 0:
        print(f"[+] Port {port} is OPEN")
    s.close()
    

if __name__ == "__main__":
    target = input("Enter target IP: ").strip()
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))

    print(f"\nScanning {target} for open ports...\n")
    
    for port in range(start_port, end_port + 1):
        scan_port(target, port)

    print("Scan complete!")


