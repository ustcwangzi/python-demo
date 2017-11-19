"""
 数字格式化
"""


def run():
    x = 1234.56789
    # Two decimal places of accuracy
    print(format(x, '0.2f'))

    # Right justified in 10 chars, one-digit accuracy
    print(format(x, '>10.1f'))

    # Left justified
    print(format(x, '<10.1f'))

    # Centered
    print(format(x, '^10.1f'))

    # Inclusion of thousands separator
    print(format(x, ','))
    print(format(x, '0,.1f'))

    # 科学记数法
    print(format(x, 'e'))
    print(format(x, '0.2E'))

    # strings
    print('The value is {:0,.2f}'.format(x))


if __name__ == '__main__':
    run()
