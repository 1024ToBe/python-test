#文本文件的备份
#需求: 编写一个程序,完成电脑上任意文件的备份操作
# 分析: 要完成任意文件,读写模式都应该选择通用的二进制模式
# 1.打开文件
# 注意: 以下file.mp4演示是视频复制,也可以改为图片,文本等文件
# 视频 / 图片属于二进制，不能用 r/w，必须 rb/wb
'''
#打开源文件 rb二进制读
f_in = open('sources/file.mp4', 'rb')
#f_in = open('sources/girl.png', 'rb')
#目标文件 wb二进制写
f_out = open('backup/file[备份].mp4', 'wb')
#f_out = open('backup/girl[备份].png', 'wb')

# 2.读写文件
# 先读取源文件
data = f_in.read()
# 再把源文件数据写入到备份文件
f_out.write(data)
# 3.关闭文件
# 思路: 先开后关
f_out.close()
f_in.close()
'''

# 先定义函数
# 先选中函数体内容再按ctrl+alt+m快速抽取出函数
def file_copy(in_path):
    # 获取输出路径
    i = in_path.rfind('.')
    if i == -1:
        print('对不起,您输入的文件路径无效!!!')
    else:
        out_path = in_path[:i] + "[备份]" + in_path[i:]
        print(out_path)
        # 打开文件
        f1 = open(in_path, 'rb')
        f2 = open(out_path, 'wb')
        # 备份文件(先读再写)
        data = f1.read()
        f2.write(data)
        # 关闭文件(先开后关)
        f2.close()
        f1.close()


# 调用函数
in_path = input('请您输入要备份的文件路径:')
file_copy(in_path)