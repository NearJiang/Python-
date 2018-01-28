#在Python中，读写文件这样的资源要特别注意，必须在使用完毕后正确关闭它们。
#正确关闭文件资源的一个方法是使用try...finally：

try:
    f = open('/path/to/file', 'r')
    f.read()
finally:
    if f:
        f.close()
#写try...finally非常繁琐。
#Python的with语句允许我们非常方便地使用资源，而不必担心资源没有关闭，
        #所以上面的代码可以简化为：

with open('/path/to/file', 'r') as f:
    f.read()
