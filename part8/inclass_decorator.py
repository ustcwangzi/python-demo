"""
 在类中定义包装器
"""
from functools import wraps


class A:
    # 作为实例方法
    def decorator1(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Decorator 1')
            return func(*args, **kwargs)
        return wrapper

    # 作为类方法
    @classmethod
    def decorator2(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Decorator 2')
            return func(*args, **kwargs)
        return wrapper


a = A()
@a.decorator1
def spam1():
    print("Spam1")


@A.decorator2
def spam2():
    print("Spam2")


def run():
    spam1()
    spam2()


if __name__ == '__main__':
    run()
