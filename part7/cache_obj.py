"""
 创建缓存实例，相同参数创建的对象是同一个
 WeakValueDictionary实例只保存在其他地方还被使用的实例
"""
import weakref


class CacheManager:
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()

    def get_spam(self, name):
        if name not in self._cache:
            temp = Spam._new(name)
            self._cache[name] = temp
        else:
            temp = self._cache[name]
        return temp

    def clear(self):
        self._cache.clear()


class Spam:
    def __init__(self, *args, **kwargs):
        raise RuntimeError("Can't instantiate directly")

    @classmethod
    def _new(cls, name):
        self = cls.__new__(cls)
        self.name = name
        return self


def run():
    a = Spam._new('Dav')
    b = Spam._new('Dav')
    print(a is b)

    manager = CacheManager()
    s = manager.get_spam('Tom')
    t = manager.get_spam('Tom')
    print(s is t)


if __name__ == '__main__':
    run()
