import subprocess
import sys

def ping_host_secure(host_address):
    """
    Pings a host securely using the subprocess module.
    """
    try:
        # Pass the command and arguments as a list.
        # This prevents command injection as the shell does not interpret the input.
        subprocess.run(['ping', '-c', '4', host_address], check=True)
    except FileNotFoundError:
        print("Error: The 'ping' command was not found.")
    except subprocess.CalledProcessError as e:
        print(f"Error: Command failed with exit code {e.returncode}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python secure_script.py <hostname>")
        sys.exit(1)

    hostname = sys.argv[1]
    print(f"Pinging {hostname}...")
    ping_host_secure(hostname)
