#Unix/Linux操作系统提供了一个fork()系统调用
#它非常特殊。普通的函数调用，调用一次，返回一次，但是fork()调用一次，返回两次
#因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程）
#然后，分别在父进程和子进程内返回
import os

print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac:
pid = os.fork()
if pid == 0:#如果返回0（子进程永远返回0，而父进程返回子进程的ID）
    print('I am child process (%s) and my dad is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
    
    #子进程只需要调用getppid()就可以拿到父进程的ID
    #我是dad是getpid，我儿子就是pid
    #我是儿子getpid，我dad就是getppid

#！！！！！windows玩不了fork,呵呵呵！欺负穷逼！拜拜了您！
