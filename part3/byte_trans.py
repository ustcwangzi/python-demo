"""
 大整数与字节的相互转换
"""


def run():
    data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
    print(len(data))
    # big／little指字节顺序
    print(int.from_bytes(data, 'little'))
    print(int.from_bytes(data, 'big'))

    x = 94522842520747284487117727783387188
    print(x.to_bytes(16, 'big'))
    print(x.to_bytes(16, 'little'))
    print(x.to_bytes(20, 'big'))


if __name__ == '__main__':
    run()
