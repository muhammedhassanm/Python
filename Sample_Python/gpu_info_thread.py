# -*- coding: utf-8 -*-
'''
Created on Mon Feb 10 17:24:55 2020

@author: 100119
'''

import os
import time
import psutil
import GPUtil
import pandas as pd
from threading import Thread
GPUtil.showUtilization()

#print('GPU RAM Free: {0:.0f}MB | Used: {1:.0f}MB | Util {2:3.0f}% | Total {3:.0f}MB'.format(gpu.memoryFree, gpu.memoryUsed, gpu.memoryUtil*100, gpu.memoryTotal))
#extra_columns  = ['GID','GPU RAM FREE','GPU RAM USED','GPU Utilisation','TOTAL MEMORY USED']
p = psutil.Process(os.getpid())
LOG_LIST = []

class Monitor(Thread):
    def __init__(self, delay):
        self.df = pd.DataFrame()
        super(Monitor, self).__init__()
        self.stopped = False
        self.delay = delay # Time between calls to GPUtil
        self.start()
    
    def run(self):
        while not self.stopped:
            try:
    #                GPUtil.showUtilization(all=True)
    #                GPUs = GPUtil.getGPUs()
    #                gpu = GPUs[0]
                t = time.localtime()
                current_time = time.strftime('%H:%M:%S', t)
                
                LOG_LIST.append([current_time,p.pid,p.name(),p.cpu_percent(),p.memory_percent(),\
                                 'NAN','NAN','NAN','NAN','NAN'])
    #            df.loc[len(df)] = LOG_LIST[0]
                df= self.df.append(LOG_LIST,ignore_index=True)
                print(df)
                df.to_csv('log_csv.csv',header  = ['Time','PID','NAME','CPU Utilization(%)','CPU RAM USED(%)',\
                                                   'GID','GPU RAM FREE','GPU RAM USED','GPU Utilisation','TOTAL MEMORY USED'])
                time.sleep(self.delay)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
                
    def stop(self):
        self.stopped = False
        


monitor = Monitor(10)

# Train, etc.

# Close monitor
monitor.stop()



