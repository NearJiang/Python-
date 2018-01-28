import pickle
d = dict(name='Bob', age=20, score=88)
pickle.dumps(d)
#pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。
#或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object
f= open('dump.txt','wb')
pickle.dump(d.f)
f.close()

f= open('dump.txt','rb')
d= pickle.load(f)
f.close()
