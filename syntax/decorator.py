# ======decorator=======
# 装饰器（decorator）可以给函数动态加上功能


# @property装饰器就是负责把一个方法变成属性调用
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

# @staticmethod将函数转换成为一个静态方法
    @staticmethod
    def calculateScore(x: int, y: int):
        score = 0.5*x + 0.5*y
        return score
