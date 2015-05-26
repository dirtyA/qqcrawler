# -*- coding:utf-8 -*-
"""
qq种子生产模块
输入:qq号码区间
输出:qq号队列
"""

import time
import threading
import log
import redis

logger = log.Logger(logname='log.txt', loglevel='DEBUG', logger="fox").getlog()


class QQSeed(threading.Thread):
    def __init__(self, r, seed_List, startNum, endNum ):
        """
        初始化
        """
        threading.Thread.__init__(self )

        self.r = r
        self.seed_List = seed_List
        self.startNum = startNum
        self.endNum = endNum
        self.flag = True    #标记


    def run(self):

        logger.info('QQ种子生成线程启动')

        counter = int(self.startNum)  #计数器起始qq
        elm = self.startNum

        while counter <= int(self.endNum):

            self.r.rpush(self.seed_List, str(elm))

            elm = int(elm) + 1
            counter = counter + 1




def main():
    r = redis.Redis( host= "localhost", port = 6379, db = 0)
    r.flushdb()
    seed_List = []
    startNum = 100000
    endNum = 110000
    pp = QQSeed(r, seed_List, startNum, endNum)
    pp.start()









