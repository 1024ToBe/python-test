import re

# 匹配HTML标签
s = "<h1>编程语言</h1>啦啦啦啦啦啦啦<h1>Python代码</h1>"

p1 = r'<h1>.*</h1>'  #贪婪模式，输出符合规则的最长子串
p2 = r'<h1>.*?</h1>'  #贪婪模式，输出符合规则的最短子串
r1 = re.match(p1,s)
r2 = re.match(p2,s)
print('贪婪模式:',r1.group(),'\n非贪婪模式：',r2.group())
