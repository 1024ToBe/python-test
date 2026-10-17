name = '赵'
name_byte = name.encode('UTF-8')
print(name_byte,type(name_byte))

name2 = name_byte.decode("UTF-8")
print(name2)

'''
# UTF8
#周->\xe5\x91\xa8->111001010101001 1001 101000
#1个二进制1个bit,8个二进制1个byte
#在UTF8一个中文转为3个byte(24个二进制)

# GBK
# GBK
一个中文占用2个byte,16个二进制数字
#周->100011111111111111
#1byte=8个0或1
# 1024 byte = 1KB
# 1024KB = 1MB
# 1024MB
TITT
= 1GB
'''
name = 'itheima'
# name是字符串

bytes = b'itheima'
# bytes就是二进制对象

print(bytes)