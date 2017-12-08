"""
 带状态值的回调函数
"""


def add(x, y):
    return x + y


def apply_async(func, *args, callback):
    result = func(*args)
    callback(result)


# 类方式
class ResultHandler:
    def __init__(self):
        self.sequence = 0

    def handler(self, result):
        self.sequence += 1
        print('[{}] Got: {}'.format(self.sequence, result))


# 闭包方式
def make_handler():
    sequence = 0

    def handler(result):
        nonlocal sequence
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))
    return handler


def run():
    r = ResultHandler()
    apply_async(add, 2, 3, callback=r.handler)
    apply_async(add, 'hello', 'world', callback=r.handler)

    handler = make_handler()
    apply_async(add, 2, 3, callback=handler)
    apply_async(add, 'hello', 'world', callback=handler)


if __name__ == '__main__':
    run()
