# -*- coding:utf-8 -*-
"""
    qq信息抓取系统
    其中，
    seed_List, task_List, 种子和任务存放在内存数据库r中
    result_Queue 爬取解析结果存放到队里中
    visited_Set 被访问的qq号存入元组中
"""

import Queue
import data_Store
import qqSeed_Base
import url_Fetcher_Parser
import url_Filter
import sys
import getopt
import redis

def usage():
        """
        用作帮助提示信息
        """
        print sys.argv[0] + ' -s startNum -e endNum'
        print sys.argv[0] + ' -h #get help info'

def main():

    r = redis.Redis(host = "localhost", port = 6379, db = 2)
    r.flushdb()

    seed_List = []
    task_List = []
    qqVisitedSet = set()
    qqResultQueue =Queue.Queue()

    type = 1
    startNum = ''
    endNum = ''

    opts,args = getopt.getopt(sys.argv[1:], 'hs:e:',['help', 'startNum=', 'endNum='] )
    for op,value in opts:
        if op == '-s' or op == '-startNum':
            startNum = value
        elif op == '-e' or op == '-endNum':
           endNum = value
        elif op == '-h':
            usage()
            sys.exit()

    #种子生成
    seed = qqSeed_Base.QQSeed(r, seed_List, startNum, endNum)
    seed.start()

    #过滤
    qq = url_Filter.QQFilter(r, seed_List, task_List, qqVisitedSet)
    qq.start()

    #爬虫解析
    fp1 = url_Fetcher_Parser.QQFetPar(r, task_List, qqVisitedSet, qqResultQueue, type)
    fp1.start()

    fp2 = url_Fetcher_Parser.QQFetPar(r, task_List, qqVisitedSet, qqResultQueue, type)
    fp2.start()

    fp3 = url_Fetcher_Parser.QQFetPar(r, task_List, qqVisitedSet, qqResultQueue, type)
    fp3.start()

    fp4 = url_Fetcher_Parser.QQFetPar(r, task_List, qqVisitedSet, qqResultQueue, type)
    fp4.start()

    #数据存储
    data = data_Store.DataStore(qqResultQueue, type)
    data.start()



if __name__ == '__main__':
    main()


