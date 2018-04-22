"""
 利用装饰器检查函数的入参类型
 bind_partial执行从指定类型到名称的部分绑定，缺失的参数会被忽略，
 此时会创建一个有序的字典，这个字段将参数名以函数签名中的形同顺序映射到指定类型上
 bind和bind_partial类似，但不会忽略任何参数
"""
from functools import wraps
from inspect import signature


def typeassert(*ty_args, **ty_kwargs):
    def decorate(func):
        sig = signature(func)
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError(
                            'Argument {} must be {}'.format(name, bound_types[name])
                        )

            return func(*args, **kwargs)

        return wrapper

    return decorate


@typeassert(int, int)
def add(x, y):
    print(x + y)


@typeassert(int, z=int)
def spam(x, y, z=20):
    print(x, y, z)


def run():
    add(1, 2)
    #add(1, '22')
    spam(1, 2, 3)
    spam(1, '22')
    #spam('11', '22')
    #spam(1, 2, 'hello')


if __name__ == '__main__':
    run()
