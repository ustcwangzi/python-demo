"""
 默认参数
"""


def fun1(a, b=22):
    print(a, b)


# 这种方式不可取，会影响后面的结果
def fun2(a, b=[]):
    b.append(a)
    return b


def run():
    fun1(1)
    fun1(1, 2)
    print(fun2('first'))
    print(fun2('second'))


if __name__ == '__main__':
    run()
