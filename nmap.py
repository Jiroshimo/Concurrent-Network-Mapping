import nmap

nm = nmap.PortScanner(nmap_search_path=('/usr/bin/nmap',))

print("Scanning network for ports and OS... please wait...")
# Added -O for OS detection
nm.scan(hosts='192.168.1.1/24', arguments='-p 22,80,443 -O -T4 --max-retries 1')

for host in nm.all_hosts():
    print(f"\nHost: {host} ({nm[host].hostname()})")
    print(f"Status: {nm[host].state()}")
    
    # --- NEW: Check for OS Matches ---
    # Nmap returns a list of possible OS matches. We'll grab the most likely one.
    if 'osmatch' in nm[host] and len(nm[host]['osmatch']) > 0:
        best_match = nm[host]['osmatch'][0]
        os_name = best_match.get('name', 'Unknown')
        accuracy = best_match.get('accuracy', '0')
        print(f"OS Guess: {os_name} ({accuracy}% accuracy)")
    else:
        print("OS Guess: Could not determine OS")
    # ---------------------------------
    
    for proto in nm[host].all_protocols():
        ports = nm[host][proto].keys()
        for port in ports:
            state = nm[host][proto][port]['state']
            print(f"  - Port {port}: {state}")
