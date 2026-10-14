'''
open函数参数1file:文件路径
    绝对路径: 以盘符开头的路径
    相对路径: 不以盘符开头的路径  .当前目录  ..上一级目录
open函数参数2mode: 文件模式
    r: 读(默认)    rb:二进制读    特点: 文件必须存在,否则报错
    w: 写         wb:二进制写    特点: 文件如果存在就使用,不存在就创建
    a: 追加       ab:二进制追加写 特点: 文件如果存在就使用,不存在就创建
open函数参数3encoding: 文件编码
    注意: 二进制相关模式不需要文件编码了...,否则报错ValueError: binary mode doesn't take an encoding argument
    gbk: 主要针对中文扩展 ,又叫cp936
    utf8: 通用编码 ,又叫万国码
'''

# 1.打开文件
f = open('word.txt', mode='r', encoding='utf8')
#open()` 返回的**是文件对象（文件句柄）**，**不是文件里面的文字内容**
print(f)

#打印文本内容
content = f.read()
print(content)

# 2.读写文件(本次略)
# 3.关闭文件
#open()打开文件，会占用操作系统的文件资源；f.close()就是释放这个资源，归还给操作系统。
f.close()

'''
读模式:
r: 读非二进制格式数据
rb: 读二进制格式数据
字符串转二进制: 字符串.encode(编码)
二进制转字符串: 二进制.decode(编码)

一个个读:
read(num): 读n个字符
read(): 读剩下的所有字符

一行行读:
readline(): 读一行
readlines(): 读剩下的所有行
注意: 默认放到列表中返回
'''
# 1.打开文件
# 注意:如果读取非文本文件,则需要指定mode='rb',且不能添加encoding参数
f = open('word.txt', 'r', encoding='utf8')
# 2.读文件
# #方式1: read(num) 一个个读,读取指定num个字符
# content = f.read(7)
# print(content)
# print('---------------------------')

# 方式2: read() 一个个读,默认读取所有字符
# content = f.read()
# print(content)
# print('---------------------------')

# 方式3: readline() 一行行读,读取一行
# content = f.readline()
# print(content)
# print('---------------------------')

# 方式4: readlines() 一行行读,一次性读取所有行
content = f.readlines()
print(content)
# 3.关闭文件
f.close()


#4.文件的写操作
'''
写模式:
	w: 非二进制格式数据,覆盖写
	rb: 二进制格式数据,覆盖写,
	rb: 读出来的是 bytes 字节，不是字符串，不能 print 直接看
	wb: 写入的必须是bytes类型
    a: 非二进制格式数据,追加写
	ab: 二进制格式数据,追加写
	字符串转二进制: 字符串.encode(编码)
	二进制转字符串: 二进制.decode(编码)
一个个写:write(内容)
一行行写:writelines(内容)
'''

'''
# 1.打开文件
f = open('new_word.txt', 'w', encoding='utf8')
# 2.写数据到文件
f.write('hello world\n')
f.writelines(['你好\n', 'python\n','文件操作\n'])
# 3.关闭文件
f.close()
'''

# f = open() : 必须手动关闭文件,也可能受异常影响导致没有执行到关闭代码
# with open() as f : 自动关闭文件,不会受异常影响
# 需求: 使用with方式读取文件内容
with open('word.txt', 'r', encoding='utf8') as f_in:
    data = f_in.read()
    print('with open打开模式：\n',data)
'''
等同于传统写法
f_in = open('word.txt', 'r', encoding='utf8')
data = f_in.read()
print(data)
f_in.close()
'''



