#如果要启动大量的子进程，可以用进程池的方式批量创建子进程

from multiprocessing import Pool
import os, time, random

def timer(name):
    print('Run task %s (%s)...' %(name,os.getpid()))
    start=time.time()
    time.sleep(random.random()*3)
    end=time.time()
    print('Task %s runs %0.2f seconds' % (name,(end-start)))

if __name__=='__main__':
    print('Dad process %s'%os.getpid())
    p = Pool(4)#因为Pool的默认大小是你电脑几核cpu
    for i in range(5):
        p.apply_async(timer,args=(i,))
    print('Waiting...')
    p.close()
    p.join()
    print('All subprocesses done')
#然后我们的Pool好像也不怎么看得上windows，啊哈哈哈！！！穷loser不要学python了！
    #理想执行结果：
Dad process 669
Waiting...
Run task 0 (671)...
Run task 1 (672)...
Run task 2 (673)...
Run task 3 (674)...
Task 2 runs 0.14 seconds.
Run task 4 (673)...
Task 1 runs 0.27 seconds.
Task 3 runs 0.86 seconds.
Task 0 runs 1.41 seconds.
Task 4 runs 1.91 seconds.
All subprocesses done
   
