"""
 使用闭包将单方法类转换为函数
 一个闭包就是一个函数，只不过在函数内部带上了额外的变量环境，
 闭包的特点是会记住自己被定义时的环境，并在接下来的调用中使用它
"""


class StrUtils:
    def __init__(self, arg):
        self.arg = arg

    def tolow(self, name):
        return (self.arg + name).lower()


# 闭包方式
def strutils(arg):
    def tolow(name):
        return (arg + name).lower()
    return tolow


def run():
    util = StrUtils("HELLO ")
    result = util.tolow("PYTHON")
    print(result)

    result = strutils("HELLO ")
    print(result("PYTHON"))


if __name__ == '__main__':
    run()
