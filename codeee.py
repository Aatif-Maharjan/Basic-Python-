import paramiko
import socket
import sys

# List of vulnerable OpenSSH versions (CVE-2025-26465, CVE-2025-26466)
VULNERABLE_VERSIONS = [f"OpenSSH_{v}p1" for v in range(6, 10)]  

def get_ssh_banner(target, port=22):
    try:
        sock = socket.socket()
        sock.settimeout(5)
        sock.connect((target, port))
        banner = sock.recv(1024).decode().strip()
        sock.close()
        return banner
    except Exception as e:
        return f"Error: {e}"

def check_vulnerability(target, port=22):
    banner = get_ssh_banner(target, port)
    
    if "OpenSSH" in banner:
        print(f"[+] Target {target} is running {banner}")
        
        # Check if OpenSSH version is vulnerable
        for version in VULNERABLE_VERSIONS:
            if version in banner:
                print(f"[!] {target} is potentially vulnerable! ({banner})")
                print(f"[!] Recommended: Upgrade to OpenSSH 9.9p2 or later.")
                return True
        print(f"[-] {target} is NOT running a known vulnerable OpenSSH version.")
    else:
        print(f"[-] Could not retrieve SSH banner from {target}.")
    
    return False

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 ssh_vuln_scanner.py <target-ip>")
        sys.exit(1)
    
    target = sys.argv[1]
    check_vulnerability(target)

if __name__ == "__main__":
    main()
