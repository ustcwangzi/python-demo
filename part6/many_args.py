"""
 位置参数／关键字参数
"""


# 接收任意数量的位置参数
def fun1(first, *rest):
    val = (first + sum(rest)) / (1 + len(rest))
    print(val)


# 接收任意数量的关键字参数
def fun2(name, school, **kwargs):
    print(name, school)
    for k, v in kwargs.items():
        print(k, v)


# 同时使用位置参数和关键字参数
# *参数后可定义其他参数，**参数只能放在最后一个位置
def fun3(*args, **kwargs):
    print(args)
    print(kwargs)


# 强制使用关键字参数，将关键字参数放在*参数后即可
def fun4(size, *, block):
    print("Hello, Python")


def run():
    fun1(1, 2, 5, 8, 9)
    fun2('wang', 'ustc', city='Shanghai', gender='M', job='Engineer')
    fun3('wang', 'ustc', 26, city='Shanghai', gender='M', job='Engineer')
    # 这两种方式均报错
    # fun4(1024, 'wang')
    # fun4(1024, 'wang', block=True)
    # 这种方式正确
    fun4(1024, block=True)


if __name__ == '__main__':
    run()
