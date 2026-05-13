# Port Status Checker
# Checks whether a specific port on a system is OPEN or CLOSED

import socket

# Take inputs from user
host = input("Enter host/IP address: ")
port = int(input("Enter port number: "))

try:
    # Create socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Set timeout (in seconds)
    s.settimeout(3)

    # Try connecting to the port
    result = s.connect_ex((host, port))

    # Check result
    if result == 0:
        print(f"Port {port} is OPEN on {host}")
    else:
        print(f"Port {port} is CLOSED on {host}")

    # Close socket
    s.close()

except socket.gaierror:
    print("Invalid host or IP address")

except ValueError:
    print("Please enter a valid port number")

except Exception as e:
    print("Error:", e)