#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
my_list =[1,2,3,4,5]
print(list(map(str, my_list)))

print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

print(sum(my_list))

from functools import reduce
def fn(x, y):
  return x*10 + y

print(reduce(fn, my_list))

def char2num(s):
  return {'0': 0, '1': 1, '2': 2, '3': 3, \
  '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
print(char2num('1'))


def normalize(name):
    name = name.lower()
    return name.capitalize()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

print(ord('A'))
print(chr(65))


s1 = 72
s2 = 85
r = (s2 - s1) / s1 * 100
print("advance %.1f%%" % r)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

# 打印Apple:
print("Apple = %s" % L[0][0])
# 打印Python:
print("Python = %s" % L[1][1])
# 打印Lisa:
print("Lisa = %s" % L[2][2])


L = ['Bart', 'Lisa', 'Adam']
for x in L:
  print("hello %s" % x)

n1 = 255
n2 = 1000
print(hex(n1), hex(n2))


import math

def quadratic(a, b, c):
  n = b*b -4*a*c;
  if n>0:
    first = (-b+math.sqrt(n))/(2*a)
    sec = (-b-math.sqrt(n))/(2*a)
    return [first, sec]

# 测试:ax2 + bx + c = 0 的二个解
print(quadratic(2, 3, 1)) # => (-0.5, -1.0)
print(quadratic(1, 3, -4)) # => (1.0, -4.0)

def add_end(L=None):
  if L is None:
    L = []
  L.append('End')
  return L

print(add_end())
print(add_end())

def hello(greeting, *args):
  if (len(args) == 0):
    print("%s !" % greeting)
  else:
    print("%s, %s!" % (greeting, ','.join(args)))

hello('Hi') # => greeting='Hi', args=()
hello('Hi', 'Sarah') # => greeting='Hi', args=('Sarah')
hello('Hello', 'Michael', 'Bob', 'Adam') # => greeting='Hello', args=('Michael', 'Bob', 'Adam')

names = ('Bart', 'Lisa')
hello('Hello', *names) # => greeting='Hello', args=('Bart', 'Lisa')

#请编写move(n, a, b, c)函数，它接收参数n，
#表示3个柱子A、B、C中第1个柱子A的盘子数量，
#然后打印出把所有盘子从A借助B移动到C的方法，例如：


def move(n, a, b, c):
  if(n==1):
    print(a, "--> ", c)
  else:
    move(n-1, a, c, b)
    move(1, a, b, c)
    move(n-1, b, a, c)

# 期待输出:
# A --> C
# A --> B
# C --> B
# A --> C
# B --> A
# B --> C
# A --> C
move(3, 'A', 'B', 'C')

class objA:
  pass

A = objA()
B = 'a', 'b'
C = 'a is string'

print(isinstance(A, objA))
print(isinstance(B, tuple))
print(isinstance(C, str))

import copy

al = [[1],[2],[3]]
bl = copy.copy(al)
cl = copy.deepcopy(al)

print("before=>")
print(al)
print(bl)
print(cl)

al[0][0] = 0
al[1] = None

print("after=>")
print(al)
print(bl)
print(cl)

import os
def GetFile(directoryName, extend):
  for root, directoryList, fileList in os.walk(directoryName):
    for fileName in fileList:
      root, extension = os.path.splitext(fileName)
      if extension == extend:
        print(fileName)
    for directoryName in directoryList:
      GetFile(directoryName, extend)

GetFile("d:/", ".json")


import threading, multiprocessing
def loop():
  print('thread %s is running...' % threading.current_thread().name)
  n = 0
  while n < 5:
      n = n + 1
      print('thread %s >>> %s' % (threading.current_thread().name, n))
      time.sleep(1)
  print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)


def triangle(n):
    L=[1]
    while True:
        yield(L)
        L.append(0)
        L=[L[i]+L[i-1] for i in range(len(L))]
        if len(L)>10:
            break
    return "done"

g=triangle(10)
for i in g:
    print(i)



import asyncio

@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()



import time
import datetime

now = datetime.datetime.now()
now.strftime('%Y-%m-%d %H:%M:%S')
print(now)

s=u'龚鹏奥斯'
print(s)


from urllib import request, parse

# get:


req = request.Request('https://api.douban.com/v2/book/2129650')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))


import re


# 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
match = re.search(r'h\Dllo', 'hallo world!, hgllo')

if match:
    # 使用Match获得分组信息
    print(match.group())


class Fabs(object):
  def __init__(self, max):
    self.max = max
    self.n, self.a, self.b = 0, 0, 1

  def __iter__(self):
    return self

  def next(self):
    if self.n < self.max:
      r = self.b

      self.n, self.a, self.b = self.n + 1, self.b, self.a + self.b
      return r
    raise StopIteration()
print(Fabs(5))
for key in Fabs(5):
  print(key)


class Fabs(object):
    def __init__(self,max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1  #特别指出：第0项是0，第1项是第一个1.整个数列从1开始
    def __iter__(self):
        return self
    def __next__(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n = self.n + 1
            return r
        raise StopIteration()

#print(Fabs(5))
for key in Fabs(5):
    print(key)
'''
from collections import defaultdict
boys=['gong', 'peng', 'rong']
girls=['parse', 'raise', 'geng']
girlMap = {}
for key in girls:
  girlMap.setdefault(key[0],[]).append(key)
print([boy+'+'+''.join(girlMap[boy[0]]) for boy in boys])


