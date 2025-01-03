import psutil
import requests
import os
import logging
import configparser

list_psutil=['host_info','network','disk','memory','cpu','load']

host_info=['os','hostname','boot_time']
network=['list','interface','mtu']
disk=['disk','mountpoint','fs','used','total']
memory=['mem_total','mem_used','mem_percent']
cpu=['cpu_cores','cpu_phys','cpu_freq']
load=['1 min','5 min', '15 min']