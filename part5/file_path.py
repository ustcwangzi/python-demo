"""
 文件路径
"""
import os


def run():
    path = '/Users/wangzi/Downloads/algs4.jar'
    # 文件名
    print(os.path.basename(path))
    # 路径名
    print(os.path.dirname(path))
    # 文件与后缀分开
    print(os.path.splitext(path))
    # 检查文件是否存在
    print(os.path.exists(path))
    # 检查是否是文件
    print(os.path.isfile(path))
    # 文件大小
    print(os.path.getsize(path))
    # 路径拼接，自动适应当前文件系统
    newPath = os.path.join('tmp', 'data', os.path.basename(path))
    print(newPath)
    # 列出目录下的文件
    print(os.listdir('/Users/wangzi/'))


if __name__ == '__main__':
    run()
