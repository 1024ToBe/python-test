import re

s = 'ITheiMa'
p = r'itheima'
r = re.match(p,s,re.I) #re.I:忽略大小写
print(r.group())

s = 'it\nheima'
p = r'it.heima'
r = re.match(p,s,re.S) #re.S:规则中的 .  可以匹配\n;   .原本默认无法匹配回车符
print(r.group())
