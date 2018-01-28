from multiprocessing import Process
#文件名不要和模块一样，像这个命名为multiprocessing.py就不行
import os

#定义子程序要执行的代码
def myson(name):
    print('RUN son process %s (s)...'%(name,os.getpid()))

if __name__=='__main__':#__name__ 是当前模块名，当模块被直接运行时模块名为 __main__
#当模块被直接运行时，以下代码块将被运行，当模块是被导入时，代码块不被运行    
    print('Dad process %s'%os.getpid())
    print('Son process will start')
    s=Process(target=myson,args=('qibaobao',))
    s.start()
    s.join()#等待子进程son process结束后再继续往下运行
    print('Son process end')

#修改了名字还运行不了，就去刚生成的__pycache__，把里面的multiprocessing.pyc文件删除
