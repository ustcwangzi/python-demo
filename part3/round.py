"""
 四舍五入
"""


def run():
    # 四舍五入
    print(round(1.23, 1))

    # 当一个值刚好在两个边界中间时，返回离它最近的偶数
    print(round(1.5))
    print(round(2.5))

    # 传入负数时，作用在十位／百位／...上面
    print(round(123456, -2))


if __name__ == '__main__':
    run()
