import socket
import netifaces
import concurrent.futures


def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Connects to a dummy address to find the active network interface
        s.connect(('8.8.8.8', 1))
        local_ip = s.getsockname()[0]  # [0] extracts ONLY the IP address string
    except Exception:
        local_ip = '127.0.0.1'
    finally:
        s.close()
    return local_ip

print(f"Your Local Network IP Address: {get_local_ip()}\n")

def get_default_gateway(): # using netifaces
    gateways = netifaces.gateways()
    # Fetch the default IPv4 gateway entry
    default_gw = gateways.get('default', {}).get(netifaces.AF_INET)

    if default_gw:
        return default_gw[0] # The first element is the IP address string
    return "No default gateway found"

print(f"Your Default Gateway: {get_default_gateway()}")



