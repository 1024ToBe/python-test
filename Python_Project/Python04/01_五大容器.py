name_list = ['张三','李四','王五']
print(name_list)

#1.空字符串
s1 = ''
s2 = ""
s3 = """"""
print(type(s1),type(s2),type(s3))

#2.非空字符串
s4 = '黑马进阶，晋级高薪资，加油，高薪'
#打印字符长度
print(len(s4))
#打印子字符出现次数
print(s4.count('高薪'))
#打印子字符出现次数
print(s4.index('晋'))

#3.替换
s5 = '我今天心情很emo,emo'
s6 = s5.replace('emo','happy',1)
print(s6,s5)

#4.切割
s7 = '猕猴桃、橘子、橙子、榴莲'
list = s7.split('、')
print(s7,list)

#5.拼接
s8 = '猕猴桃、橘子、橙子、榴莲'
s9 = s8.join('芒果、')
print(s9)

#6.遍历
s10 = '猕猴桃、橘子、橙子、榴莲'
for e in s10:
    print(e)
print('=================')

index = 0
while index < len(s10):
    print(s10[index])
    index+=1