import platform

ipv4 = r"((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.)"
ipv4 += r"{3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"
ipv4_pattern = ipv4 + r"\/(3[0-2]|[12]?[0-9])"
ipv6 = r"([0-9a-fA-F]{1,4}:){1,4}:"
ipv6 += r"((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}"
ipv6 += r"(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))"

if platform.system() == "Windows":
    import wmi
    c = wmi.WMI()
    for interface in c.Win32_NetworkAdapterConfiguration(IPEnabled=True):
        print("Device Name:", interface.Description)
        print("IPv4 Address:", interface.IPAddress[0])
        print("IPv6 Address:", interface.IPAddress[1])
else:
    import subprocess
    ipconfig_process = subprocess.Popen(['ip', 'config'], stdout=subprocess.PIPE)
    ipconfig_output = ipconfig_process.stdout.read().decode('utf-8')
    ipv4_addresses = re.findall(ipv4_pattern, ipconfig_output)
    ipv6_addresses = re.findall(ipv6, ipconfig_output)
    print("IPv4 Addresses:", ipv4_addresses)
    print("IPv6 Addresses:", ipv6_addresses)
