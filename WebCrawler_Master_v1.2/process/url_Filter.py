# -*- coding:utf-8 -*-

'''
文件名：url_Filter.py
'''
import threading
import time
import Queue
import log
import redis

logger = log.Logger(logname='log.txt', loglevel='DEBUG', logger="fox").getlog()

class QQFilter(threading.Thread):
    """
    实现qq号/号码过滤功能，过滤掉已访问过的qq号码/群号
    """
    def __init__(self, r, seed_List, task_List, visited_set):
        threading.Thread.__init__(self)

        self.r = r  #内存数据库
        self.seed_List = seed_List   #种子列表
        self.task_List = task_List    #任务列表
        self.visited_set = visited_set    #已访问集合

        self.flag = True

    def run(self):
        t0 = time.time()

        logger.info('QQ检测线程启动')

        while self.flag:

            if self.r.llen(self.seed_List):
                pass

            if  self.r.llen(self.seed_List)> 0:
                qq = self.r.lpop(self.seed_List)   # 左边取 从内存数据库r 种子列表 取一个qq号
                qq = str(qq)

                if qq and qq not in self.visited_set:
                    self.r.rpush(self.task_List,qq) #右边放  将qq号放入内存数据库r 任务列表

                t0 = time.time()

            if time.time()- t0 > 20:
                self.stop()
                logger.info('QQ检测线程结束')

    def stop(self):
        self.flag = False

















