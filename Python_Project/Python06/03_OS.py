'''
os 模块: 是 Python 标准库的一部分，它提供了丰富的功能来与操作系统进行交互。
通过 os 模块，我们可以执行许多与文件和目录管理相关的操作，
比如文件重命名、文件删除。获取当前工作目录、创建和删除目录、检查文件或目录是否存在等。
'''
#1.导包
import os

#2.使用
print(os.getenv('PATH'))

# 修改文件名,注意没有返回值,文件名会直接改变
#os.rename('word.txt','test.txt')
f_out = open('backup/file[备份].mp4', 'wb')
with open('sources/file.mp4','rb') as f_in:
    data = f_in.read()
    f_out.write(data)

f_out.close()

# 删除文件
#os.remove('backup/file[备份].mp4')

#创建文件件
#os.mkdir('test')

#创建多级目录
os.makedirs('pg/bb/cc')

