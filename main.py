# -*- coding: utf-8 -*-
import sys
import signal
from multiprocessing import Process

sys.path.append('.')
sys.path.append('..')

from Api.ProxyApi import runFlask as ProxyApiRun
from Schedule.ProxyScheduler import runScheduler



def run():
    p_list = list()
    p1 = Process(target=ProxyApiRun, name='ProxyApiRun')
    p_list.append(p1)
    p2 = Process(target=runScheduler, name='runScheduler')
    p_list.append(p2)


    def kill_child_processes(signum, frame):
        for p in p_list:
            p.terminate()
        sys.exit(1)

    signal.signal(signal.SIGTERM, kill_child_processes)

    for p in p_list:
        p.daemon = True
        p.start()
    for p in p_list:
        p.join()


if __name__ == '__main__':
    run()
