"""
 不同进制之间的转换
"""


def run():
    x = 1234
    # 二进制
    print(bin(x))
    print(format(x, 'b'))
    # 八进制
    print(oct(x))
    print(format(x, 'o'))
    # 十六进制
    print(hex(x))
    print(format(x, 'x'))

    # 二进制转十进制
    print(int('10011010010', 2))
    # 八进制转十进制
    print(int('2322', 8))
    # 十六进制转十进制
    print(int('4d2', 16))


if __name__ == '__main__':
    run()
