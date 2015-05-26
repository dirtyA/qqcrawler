# -*- coding:utf-8 -*-
"""
信息存储模块
输入:以字典形式输出qq号相关信息/qq群相关信息,
    type 类型 type=1表示qq信息  type=2表示 qq群信息
输出:数据库(在mysql数据库中查看表)
"""


import log
import time
import Queue
import random
import threading

import os
import sys
from os.path import dirname
reload(sys)
sys.path.append(dirname(dirname(__file__)))
os.environ['DJANGO_SETTINGS_MODULE'] = "WebCrawler_Master.settings"

from database.models import qqInfoSave, groupInfoSave



logger = log.Logger(logname='log.txt', loglevel='DEBUG', logger="fox").getlog()

class DataStore(threading.Thread):
    def __init__(self, result_queue, type):
        threading.Thread.__init__(self)
        self.result_queue = result_queue
        self.type = type
        self.flag = True

    def run(self):
        t0 = time.time()
        logger.info('数据存储线程启动')

        while self.flag:
            if not self.result_queue.empty():
                info = self.result_queue.get()

                if self.type == 1:
                    qqInfoSave(info)
                elif self.type == 2:
                    groupInfoSave(info)

                t0 = time.time()

            else:
                time.sleep(random.randint(1, 3))

            if time.time() - t0 > 30*60:
                self.stop()
                logger.info('数据存储线程结束')

    def stop(self):
        self.flag = False

def main():
    q = Queue.Queue()
    group_info = {"name":'china', "group_number":"123456789", "qq":"943343605", "nick":" rose", "sex":" ", "position":" "}
    type = '2'
    q.put(group_info)
    kid = DataStore(q,type)
    kid.start()

if __name__ == "__main__":
    main()





