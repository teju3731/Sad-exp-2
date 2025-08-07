import os
import sys

def ping_host(host_address):
    # This is a dangerous way to build a command.
    # User input is directly concatenated into the command string.
    command = "ping -c 4 " + host_address
    
    # Executes the command. An attacker can inject malicious commands here.
    os.system(command)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python vulnerable_script.py <hostname>")
        sys.exit(1)

    hostname = sys.argv[1]
    print(f"Pinging {hostname}...")
    ping_host(hostname)
