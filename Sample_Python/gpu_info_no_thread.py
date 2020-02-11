# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 14:55:37 2020

@author: 100119
"""

import os
import time
import psutil
import GPUtil
import pandas as pd
from threading import Thread
GPUtil.showUtilization()

#print('GPU RAM Free: {0:.0f}MB | Used: {1:.0f}MB | Util {2:3.0f}% | Total {3:.0f}MB'.format(gpu.memoryFree, gpu.memoryUsed, gpu.memoryUtil*100, gpu.memoryTotal))
#extra_columns  = ['GID','GPU RAM FREE','GPU RAM USED','GPU Utilisation','TOTAL MEMORY USED']
p = psutil.Process()
LOG_LIST = []
df = pd.DataFrame()

while p.status()=='running':
    time.sleep(10)
    try:
#       GPUtil.showUtilization(all=True)
#       GPUs = GPUtil.getGPUs()
#       gpu = GPUs[0]
        t = time.localtime()
        current_time = time.strftime('%H:%M:%S', t)
        
        LOG_LIST.append([current_time,p.pid,p.name(),p.cpu_percent(),p.memory_percent(),\
                         'NAN','NAN','NAN','NAN','NAN'])
#            df.loc[len(df)] = LOG_LIST[0]
        df= df.append(LOG_LIST,ignore_index=True)
        print(df)
        df.to_csv('log_csv.csv',header  = ['Time','PID','NAME','CPU Utilization(%)','CPU RAM USED(%)',\
                                               'GID','GPU RAM FREE','GPU RAM USED','GPU Utilisation','TOTAL MEMORY USED'])
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass
                

        






