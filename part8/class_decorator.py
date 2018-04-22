"""
 将装饰器定义为类，这样装饰器可以同时工作在类定义的内部和外部
"""
import types
from functools import wraps


class Profiled:
    def __init__(self, func):
        wraps(func)(self)
        self.ncalls = 0

    def __call__(self, *args, **kwargs):
        self.ncalls += 1
        return self.__wrapped__(*args, **kwargs)

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)


@Profiled
def add(x, y):
    return x + y


class Spam:
    @Profiled
    def bar(self, x):
        print(self, x)


def run():
    add(1, 2)
    print(add(1, 2))
    print(add.ncalls)
    Spam().bar(3)
    print(Spam.bar.ncalls)


if __name__ == '__main__':
    run()
