import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)
print(json.dumps(s))
#报错

import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
        
    def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

s = Student('Bob', 20, 88)

print(json.dumps(s, default=student2dict))

#不过，下次如果遇到一个Teacher类的实例，
#照样无法序列化为JSON。我们可以偷个懒，把任意class的实例变为dict
print(json.dumps(s,default=lambda obj:obj.__dict__))
