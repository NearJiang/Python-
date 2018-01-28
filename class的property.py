class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

#把一个getter方法变成属性，只需要加上@property就可以了，
        #此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值

class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth
#@property广泛应用在类的定义中，可以让调用者写出简短的代码，
    #同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性
    
class Screen(object):
    @property         #读（getter）
    def width(self):
        return self._width
    @width.setter     #写（setter）
    def width(self,value):
        self._width = value
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,value):
        self._height = value
    @property
    def resolution(self):
        return self._width * self._height
    
