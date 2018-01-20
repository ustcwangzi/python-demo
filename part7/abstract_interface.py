"""
 抽象类
"""
from abc import ABCMeta, abstractmethod


# 不能直接实例化
class IStream(metaclass=ABCMeta):
    @abstractmethod
    def fun(self):
        pass


class SocketStream(IStream):
    def fun(self):
        pass


if __name__ == '__main__':
    # IStream() 错误
    SocketStream()
