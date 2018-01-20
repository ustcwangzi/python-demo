"""
 通过字符串调用方法
"""
import math
import operator


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, x, y):
        return math.hypot(self.x -x, self.y - y)


def run():
    # 查找属性，以函数方式调用
    p = Point(3, 4)
    d = getattr(p, 'distance')(0, 0)
    print(d)

    # 创建一个可调用的对象，并提供必要参数，调用时将实例对象传递进来
    p = Point(6, 8)
    d = operator.methodcaller('distance', 0, 0)
    print(d(p))


if __name__ == '__main__':
    run()
