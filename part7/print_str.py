"""
 实例的字符串显示
"""


class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 返回实例的代码表示，0指参数，此处为self
    # !r 指明输出使用__repr__代替默认的__str__
    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)

    # 返回实例的字符串表示，使用str()或print()时调用此方法
    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)


def run():
    p = Pair(3, 4)
    print(p)

    print('p is {0}'.format(p))
    print('p is {0!r}'.format(p))


if __name__ == '__main__':
    run()
