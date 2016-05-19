# /usr/local/bin/python3
# --*-- coding: utf-8 --*--
# __Author__ = 'Jieer'

# import  multiprocessing as mp
#
# def washer(dishes,output):
#     for dish in dishes:
#         print('Washing',dish,'dish')
#         output.put(dish)
#
# def dryer(input):
#     while True:
#         dish = input.get()
#         print('Drying',dish,'dish')
#         input.task_done()
#
# dish_queue = mp.JoinableQueue()
#
# dryer_proc = mp.Process(target=dryer,args=(dish_queue,))
# dryer_proc.daemon = True
# dryer_proc.start()
#
# dishes = ['salad','entree','dessert']
# washer(dishes,dish_queue)
# dish_queue.join()

# import threading
#
# def do_this(what):
#     whoami(what)
#
# def whoami(what):
#     print('Thread %s says:%s'%(threading.current_thread(),what))
#
# if __name__ == '__main__':
#     whoami("I'm the main program")
#     for n in range(4):
#         p = threading.Thread(target=do_this,args=("I'm function %s" % n,))
#         p.start()

#
# import threading, queue
#
# import time
#
# def washer(dishes,dish_queue):
#     for dish in dishes:
#         print("Washing",dish)
#         time.sleep(5)
#         dish_queue._put(dish)
#
# def dryer(dish_queue):
#     while True:
#         dish = dish_queue._get()
#         print('Drying',dish)
#         time.sleep(10)
#         dish_queue.task_done()
#
# dish_queue = queue.Queue
#
# for n in range(2):
#     dryer_thread = threading.Thread(target=dryer,args=(dish_queue,))
#     dryer_thread.start()
#
# dishes = ['salad','bread','entree','sesert']
#
# washer(dishes,dish_queue)
#
# dish_queue.join()

import  gevent

from gevent import socket

hosts = ['www.baidu.com','www.python.org','www.163.com']

jobs = [gevent.spawn(gevent.socket.gethostbyname,host) for host in hosts]

gevent.joinall(jobs,timeout=5)

for job in jobs:
    print(job.value)