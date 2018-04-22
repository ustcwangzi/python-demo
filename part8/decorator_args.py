"""
 接收参数的装饰器
 最外层的logged函数接收参数并将它们作用在内部的装饰器函数上，
 内层的decorate函数接收一个函数作为参数，然后在函数上放置一个包装器，
 关键点是包装器可使用logged所接收的参数
"""
import logging
from functools import wraps


def logged(level, name=None, msg=None):
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = msg if msg else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)

        return wrapper

    return decorate


@logged(logging.DEBUG)
def add(x, y):
    return x + y


@logged(logging.CRITICAL, 'example')
def spam():
    print('Spam !')


def run():
    add(1, 2)
    spam()


if __name__ == '__main__':
    run()
