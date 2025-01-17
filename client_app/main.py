import psutil
import requests
import os
import logging
import configparser
import sys
import json
import time

WORKON,conf_file='',''

def init_conf(conf_file):
    global config
    config=configparser.ConfigParser()
    config.read(conf_file)

if len(sys.argv) >= 2:
    conf_file = sys.argv[1]
else:
    conf_file = 'client.ini'

init_conf(conf_file)

def read_timeout():
    if config.get('DEFAULT','timeout'):
        timeout=int(config.get('DEFAULT','timeout'))
    else:
        timeout=20
    return timeout 

def read_ready():
    if config.get('DEFAULT','work'):
        WORKON=config.get('DEFAULT','work')
    else:
        WORKON=False
    return WORKON
    

#list_psutil=['host_info':{'os','hostname','boot_time'},\
#            'network':{'list','interface','mtu'},\
#            'disk':{'disk','mountpoint','fs','used','total'},\
#            'memory':{'mem_total','mem_used','mem_percent'},\
#            'cpu':{'cpu_cores','cpu_phys','cpu_freq'},\
#            'load':{'1 min','5 min', '15 min'}]
WORKON=read_ready()
timeout=read_timeout()
list_psutil=[['os','hostname','boot_time'],\
            ['list','interface','mtu'],\
            ['disk','mountpoint','fs','used','total'],\
            ['mem_total','mem_used','mem_percent'],\
            ['cpu_cores','cpu_phys','cpu_freq'],\
            ['1 min','5 min', '15 min']]

#host_info=['os','hostname','boot_time']
#network=['list','interface','mtu']
#disk=['disk','mountpoint','fs','used','total']
#memory=['mem_total','mem_used','mem_percent']
#cpu=['cpu_cores','cpu_phys','cpu_freq']
#load=['1 min','5 min', '15 min']
#print(timeout)
while WORKON:
    for index,l in enumerate(list_psutil):
        print(index,l)
        #for t in l:
            #print(t)   
            #print(psutil[t])



    # wait net iteration 
    time.sleep(int(timeout))