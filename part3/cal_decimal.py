"""
 浮点数精确运算
"""
from decimal import Decimal, localcontext
import math


def run():
    # 浮点数不能精确表示十进制数
    a = 4.2
    b = 2.1
    print(a + b)
    print((a + b) == 6.3)

    # 使用decimal进行精确运算
    a = Decimal('4.2')
    b = Decimal('2.1')
    print(a + b)
    print((a + b) == Decimal('6.3'))

    # decimal允许控制计算的每个方面，包括数字位数和四舍五入
    a = Decimal('1.3')
    b = Decimal('1.7')
    print(a / b)
    with localcontext() as ctx:
        ctx.prec = 3
        print(a / b)

    # sum是经过优化的，要精确运算使用fsum
    nums = [1.23e+18, 1, -1.23e+18]
    print(sum(nums))
    print(math.fsum(nums))


if __name__ == '__main__':
    run()
