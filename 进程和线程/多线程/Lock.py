#多线程和多进程最大的不同在于，
#多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，
#而多线程中，所有变量都由所有线程共享，
#所以，任何一个变量都可以被任何一个线程修改，
#因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了

import time, threading

# 假定这是你的银行存款:
balance = 0

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        change_it(n)

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
#t1和t2是交替运行的，如果操作系统以下面的顺序执行t1、t2：

初始值 balance = 0

t1: x1 = balance + 5  # x1 = 0 + 5 = 5

t2: x2 = balance + 8  # x2 = 0 + 8 = 8
t2: balance = x2      # balance = 8

t1: balance = x1      # balance = 5
t1: x1 = balance - 5  # x1 = 5 - 5 = 0
t1: balance = x1      # balance = 0

t2: x2 = balance - 8  # x2 = 0 - 8 = -8
t2: balance = x2   # balance = -8

结果 balance = -8
#要确保balance计算正确，就要给change_it()上一把锁
#创建一个锁就是通过threading.Lock()来实现

lock = threading.Lock()

def run_thread(n):
    for i in range(100000):
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()
#当多个线程同时执行lock.acquire()时，只有一个线程能成功地获取锁，
            #然后继续执行代码，其他线程就继续等待直到获得锁为止

#获得锁的线程用完后一定要释放锁，否则那些苦苦等待锁的线程将永远等待下去，
#成为死线程。所以我们用try...finally来确保锁一定会被释放

#坏处当然也很多，
#首先是阻止了多线程并发执行，包含锁的某段代码实际上只能以单线程模式执行，效率就大大地下降了
#其次，由于可以存在多个锁，不同的线程持有不同的锁，并试图获取对方持有的锁时，可能会造成死锁，
#导致多个线程全部挂起，既不能执行，也无法结束，只能靠操作系统强制终止
