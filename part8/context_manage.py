"""
 实现上下文管理器
 yield之前的代码会在上下文管理器中作为__enter__执行，
 所有yield之后的代码会作为__exit__执行，
 若出现异常，异常会在yield处抛出，
 对于一些复杂的操作要支持with功能，需要单独实现__enter__和__exit__
"""
import time
from contextlib import contextmanager


@contextmanager
def timethis(label):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print('{}: {}'.format(label, end - start))


def countdown(n):
    with timethis('counting'):
        while n > 0:
            n -= 1


def run():
    countdown(100000)


if __name__ == '__main__':
    run()
