# -*- coding:utf-8 -*-
'''
    url爬虫解析模块
    输入:qq号（从待爬取的qq号队列获取）
    输出:以字典形式输出qq号相关信息,qq群相关信息
'''

import time
import Queue
import random
import requests
import threading
import log

logger = log.Logger(logname='log.txt', loglevel='DEBUG', logger="fox").getlog()

def get_session(is_ajax = False):

    s = requests.Session()
    s.headers.update({'Referer': 'http://qun.col.pw/',
                  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36',
                  'Accept-Encoding': 'gzip,deflate,sdch'})
    s.get('http://qun.col.pw')

    if is_ajax:
        s.headers.update({'X-Requested-With': 'XMLHttpRequest'})

    return s

def getinfo1(line):
    #qq号信息
    qq_info = {"qq":' ', "nick":' ', "sex":' ', "position":' ', "group_number":' '}
    line = line.split(',')
    try:
        if line[0] != '-1':

            qq_info["qq"]= line[1].encode('utf-8')
            qq_info["nick"] = line[2].encode('utf-8')
            qq_info["sex"] = line[3].encode('utf-8')
            qq_info["position"] = line[4].encode('utf-8')
            qq_info["group_number"] = line[5].encode('utf-8')

            return qq_info
    except:
        logger.warning('没有抓取到符合条件的记录，舍弃此QQ号')
        return None


def getinfo2(line):
    #qq群信息
    group_info = {"name":' ', "group_number":"", "qq":" ", "nick":" ", "sex":" ", "position":" "}
    line = line.split(',')
    try:
        if line[0] != '-1':
            group_info["name"]= line[0].encode('utf-8')
            group_info["group_number"] = line[1].encode('utf-8')
            group_info["qq"] = line[2].encode('utf-8')
            group_info["nick"] = line[3].encode('utf-8')
            group_info["sex"] = line[4].encode('utf-8')
            group_info["position"] = line[5].encode('utf-8')

        return group_info

    except:
        logger.warning('没有抓取到符合条件的记录，舍弃此QQ群号')
        return None


class QQFetPar(threading.Thread):

    def __init__(self, r, task_List = None, visited =None, result_queue = None, type= None):
        threading.Thread.__init__(self )

        self.r = r

        self.task_List = task_List  #任务列表

        self.visited = visited
        self.result_queue = result_queue
        self.type = type
        self.flag = True

    def download(self, session, qq, kind, times=0):
        if times > 4:
            return None
        try:
            r = session.get('http://qun.col.pw/doquery.php?q=%s&type=%s' % (qq, kind))
            return r
        except Exception, e:
            logger.error(e)
            time.sleep(15)
            times = times + 1
            return self.download(session, qq, kind, times=times)

    def run(self):
        t0 = time.time()
        session = get_session(is_ajax=True)

        logger.info('QQ爬虫解析线程启动')

        while self.flag:

            if self.r.llen(self.task_List) :

                qq = self.r.lpop(self.task_List)  #从内存数据库r 任务列表  取一个qq
                qq = str(qq)

                r = self.download(session, qq, self.type)
                if not r:
                    continue

                content = r.text.split('\n')
                self.visited.add(qq)

                for line in content:
                    if not line.strip():
                        continue
                    qq_info = getinfo1(line)

                    if not qq_info:
                        continue
                    self.result_queue.put(qq_info) #把解析后的信息放到解析好的结果队列中等待存储
                t0 = time.time()
            else:
                time.sleep(random.randint(1,2))

            if time.time() - t0 > 20:
                self.stop()
                logger.info('QQ爬虫解析线程结束')

    def stop(self):
        self.flag = False




