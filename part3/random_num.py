"""
 随机数
"""
from common.data import NUMBERS
import random


def run():
    # 随机选择
    print(random.choice(NUMBERS))
    print(random.choice(NUMBERS))

    # 随机选择N个，即样本选择
    print(random.sample(NUMBERS, 2))
    print(random.sample(NUMBERS, 3))

    # 打乱元素顺序
    print(NUMBERS)
    random.shuffle(NUMBERS)
    print(NUMBERS)

    # 生成随机数
    print(random.randint(0, 10))
    print(random.randint(0, 10))

    # 生成 0-1 随机数
    print(random.random())

    # N位随机二进制数的整数返回
    print(random.getrandbits(100))

    # 修改随机数生成的种子
    # Seed based on system time or os.urandom()
    random.seed()
    # 每次运行返回值不一样
    print(random.random())
    random.seed(12345)
    # 每次运行返回值一样
    print(random.random())


if __name__ == '__main__':
    run()
