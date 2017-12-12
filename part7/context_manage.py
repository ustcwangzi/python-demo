"""
 让对象支持上下文管理器(with语句)
"""


class Connection:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.address = '127.0.0.1'
        print('开启连接 %s : %s ' % (self.name, self.address))
        return self.name

    # exc_type：异常类型，exc_val：异常值，exc_tb：追溯信息
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.address = None
        print('关闭连接 ...')


def run():
    conn = Connection('Test')
    # 当出现with语句时，__enter__会被触发，返回值赋值给as声明的变量
    # 然后with语句块里的代码开始执行，最后__exit__方法被触发
    # 不管with代码块中发生了什么，上面的控制流都会执行完，即使代码块中发生异常
    # 发生异常时，若__exit__返回True，异常信息会被清空，with语句块中的程序继续执行
    with conn as c:
        pass


if __name__ == '__main__':
    run()
