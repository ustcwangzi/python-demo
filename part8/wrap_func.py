"""
 在函数上添加包装器
 一个装饰器就是一个函数，它接收一个函数作为参数，并返回一个新的函数
 装饰器并不会修改原始函数的参数签名和返回值
"""
import time
from functools import wraps


def timethis(func):
   @wraps(func)
   def wrapper(*args, **kwargs):
       start = time.time()
       result = func(*args, ** kwargs)
       end = time.time()
       print(func.__name__, end - start)
       return result
   return wrapper


@timethis
def countdown(n: int):
    """
    Counts down
    """
    while n > 0:
        n -= 1


def run():
    countdown(100000)
    countdown(1000000)

    print(countdown.__name__)
    print(countdown.__doc__)
    print(countdown.__annotations__)
    from inspect import signature
    print(signature(countdown))


if __name__ == '__main__':
    run()
