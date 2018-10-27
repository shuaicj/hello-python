#!/usr/bin/env python3

# pip3 install psutil

# see https://github.com/giampaolo/psutil

import psutil

### cpu
print('cpu_count', psutil.cpu_count(logical=False))
print(psutil.cpu_times())

### memory
print(psutil.virtual_memory())
print(psutil.swap_memory())

### disk
print(psutil.disk_partitions())
print(psutil.disk_usage('/'))
print(psutil.disk_io_counters(perdisk=False))

### network
print(psutil.net_io_counters(pernic=True))
print(psutil.net_if_stats())

### process
# pid = 1234
# p = psutil.Process(pid)
# print(p.name())
# print(p.ppid())
# print(p.cpu_times())
# print(p.memory_info())
# print(p.io_counters())
# print(p.open_files())
# print(p.connections())
# print(p.threads())

