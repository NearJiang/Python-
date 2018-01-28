#在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private）
#只有内部可以访问，外部不能访问

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender
    def get_gender(self):   #get获取什么的 直接return就行
        return self.__gender
    def set_gender(self,gender):   #set底下要加=
        if gender not in ('male','female'):
            print('请重新输入')
        self.__gender=gender

class Student(object):

    def get_score(self):
         return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
