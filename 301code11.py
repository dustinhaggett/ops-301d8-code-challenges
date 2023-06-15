import psutil

# Get CPU times
cpu_times = psutil.cpu_times()

print(f"Time spent by normal processes executing in user mode: {cpu_times.user} seconds")
print(f"Time spent by processes executing in kernel mode: {cpu_times.system} seconds")
print(f"Time when system was idle: {cpu_times.idle} seconds")
print(f"Time spent by priority processes executing in user mode (nice): {cpu_times.nice} seconds")
print(f"Time spent waiting for I/O to complete: {cpu_times.iowait} seconds")
print(f"Time spent for servicing hardware interrupts: {cpu_times.irq} seconds")
print(f"Time spent for servicing software interrupts: {cpu_times.softirq} seconds")
print(f"Time spent by other operating systems running in a virtualized environment: {cpu_times.guest} seconds")
print(f"Time spent running a virtual CPU for guest OS under the control of the Linux kernel: {cpu_times.guest_nice} seconds")
