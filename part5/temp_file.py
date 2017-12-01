"""
 临时文件／目录，自动处理所有的创建和清理操作，文件关闭时自动删除
"""
import tempfile
from tempfile import TemporaryFile
from tempfile import TemporaryDirectory
from tempfile import NamedTemporaryFile


def run():
    # 创建匿名临时文件
    with TemporaryFile('w+t', encoding='utf-8') as f:
        f.write('Hello, Python')
        f.seek(0)
        print(f.read())

    # 创建有名称的临时文件
    with NamedTemporaryFile('w+t') as f:
        print('filename is:', f.name)

    # 创建临时目录
    with TemporaryDirectory() as dirname:
        print('dirname is:', dirname)

    # 临时文件被创建在系统的默认位置，可获取该位置
    print(tempfile.gettempdir())


if __name__ == '__main__':
    run()
