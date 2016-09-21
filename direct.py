import collections
import json
import sys
import os
from multiprocessing import Process, Pool, Queue
import time, random
import threading


def direct_test():
    favourite = collections.defaultdict(list)


def countdown(n):
    print("counting down from", n)
    while (n > 0):
        yield n
        n -= 1

def grep(str):
    print("search key", str)
    while True:
        line = yield
        if str in line:
            print(line)

def h():
    print('Wen Chuan')
    yield 5
    print('Fighting!')

def settest():
    a={'1', '2', '3'}
    b={'3', '4', '5'}
    print(a.union(b))

'''
c = h()
next(c)
x = countdown(10)
next(x)
w = grep("love")
next(w)
w.send("I love you")
w.send("I fuck you")
w.send("I kiss you")

settest()
print(os.path.expanduser('~'))
'''

def doubler(number):
    result = number * 2
    print("{0} doubler equal {1}, processId:{2}".format(
        number, result, os.getpid() ))

def multiprocess():
    numbers = [10, 20, 30, 40, 50]
    procs = []

    for index, value in enumerate(numbers):
        proc = Process(target=doubler, args=(value,))
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

def pooltest():
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))

    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')

# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)


def queuetest():
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()

def loop():
    print("thead id {0} is running".format(threading.currentThread().name))
    n = 0
    while n < 5:
        n += 1
        time.sleep(1)

    print("thead id {0} is ended".format(threading.currentThread().name))

def multithread():
    threads = []
    for i in range(5):
        t = threading.Thread(target=loop, name=i)
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

if __name__ == '__main__':
    multithread()