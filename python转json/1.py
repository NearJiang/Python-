>>> import json
>>> s='{'age':22,'score':99}'
SyntaxError: invalid syntax
>>> s='{"age":22,"score":99}'#外面有''单引号，里面要用双引号
>>> json.loads(s)#loads 把东西一件一件加载出来
{'age': 22, 'score': 99}
>>> 
>>> 
>>> d=dict(name='Near',age=20,soce=99)#Python的dict对象可以直接序列化为JSON的{}
>>> json.dumps(d)#把东西全堆在一个str里
'{"name": "Near", "age": 20, "soce": 99}'
>>> 
