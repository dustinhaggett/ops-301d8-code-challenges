import os

# Execute 'whoami' command
whoami_output = os.popen('whoami').read().strip()
print("Current user:", whoami_output)

# Execute 'ip a' command
ip_output = os.popen('ip a').read()
print("IP information:\n", ip_output)

# Execute 'lshw -short' command
lshw_output = os.popen('lshw -short').read()
print("Hardware information:\n", lshw_output)
