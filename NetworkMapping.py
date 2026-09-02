import numpy as np
import socket
import netifaces
import concurrent.futures


def get_default_gateway(): # using netifaces
        gateways = netifaces.gateways()
        # Fetch the default IPv4 gateway entry
        default_gw = gateways.get('default', {}).get(netifaces.AF_INET)

        if default_gw:
            return default_gw[0] # The first element is the IP address string
        return "No default gateway found"


all_ports_array = np.arange(65536)
gateway_ip = get_default_gateway()
print(f"Targeting Default Gateway: {gateway_ip}")

def scan_ports(port):
    

    #Initialize an IPv4 (AF_INET) AND tcp (SOCK_STREAM) socket
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Set a 0.5-second timeout so the script doesn't hang on closed ports
    scanner.settimeout(0.5)

    try:
        #connect_ex return 0 if the connection is successful (port is open)
        connection_result= scanner.connect_ex((gateway_ip, port))

        if connection_result == 0:
            #Determine the distince purpose (service name) of the open port
            try:
                service_name = socket.getservbyport(port, "tcp")
            except OSError:
                # If the port isn't in the system's known services list
                service_name = "Uknown Service"

            print(f"[+] Port {port} is OPEN | Service: {service_name}")

    except Exception as e:
        pass
    finally:
        # Always close the socket to free up system resources
        scanner.close()

if __name__ == "__main__":
    print(f"Starting scan on {gateway_ip}...")
    
    # Generate the array from 0 to 65535
    all_ports = range(65536)
    
    # Iterate through the array and pass each element to your function
    for port in all_ports:
        scan_ports(port)

