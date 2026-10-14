
'''
1.题干
定义一个参数为不定长（可变）类型的函数fun，同时传入一个列表和字典，求列表里的数字元素和字典里的value值它们的累积结果。
示例：
输入：列表[1,2,3]，字典{'a': 4,'b': 5, 'c': 6},定义一个函数fun，
输出：21
解释：它们（1+2+3+4+5+6）的累积结果=21
'''

'''
def fun(*args):
    total = 0
    lst = args[0]
    dict = args[1]

    #列表累加
    for num in lst:
        total+=num

    #字典 value 增加
    for v in dict.values():
        total+=int(v)
    return total

#函数调用
total = fun([1,2,3],{"张三":18,'李四':'20','王五':25})
print('列表值+字典 value=',total)
'''

'''
2. 题干
定义一个字符串，如str1 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"。
编写一个程序，使用随机数从字符串中抽取4个字符，用于生成验证码。
'''

'''
import  random
str1 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
code = ''
for i in  range(4):
    #从str1随机取1个字符
    ch = random.choice(str1)
    code+=ch
print('生成的四位随机验证码是：',code)
'''

'''
3. 题干
我们定义，在以下情况时，单词的大写用法是正确的：
第一种情况：全部字母都是大写，比如 "USA" 。
第二种情况：单词中所有字母都不是大写，比如 "leetcode" 。
第三种情况：如果单词不只含有一个字母，只有首字母大写， 比如 "Google" 。

给你一个字符串 word 。如果大写用法正确，返回 true ；否则，返回 false 。

示例 1：
输入：word = "USA"
输出：true

示例 2：
输入：word = "FlaG"
输出：false

提示：
1 <= word.length <= 100
word由小写和大写英文字母组成
'''
'''
def judgeStr(word):
    if word.isupper() or word.islower() or word.istitle():
        return True
    else:
        return False
# 测试
print(judgeStr("USA"))    # True
print(judgeStr("FlaG"))   # False
print(judgeStr("leetcode"))# True
print(judgeStr("Google")) # True
'''

'''
4. 题干
给你一个字符串 s 表示一个学生的出勤记录，其中的每个字符用来标记当天的出勤情况（缺勤、迟到、到场）。
记录中只含下面三种字符：

'A'：Absent，缺勤
'L'：Late ， 迟到
'P'：Present，到场
如果学生能够 同时 满足下面两个条件，则可以获得出勤奖励：

条件一：按 总出勤 计，学生缺勤（'A'）严格 少于两天。
条件二：学生 不会 存在 连续 3 天或 连续 3 天以上的迟到（'L'）记录。

如果学生可以获得出勤奖励，返回 true ；否则，返回 false 。

示例 1：
输入：s = "PPALLP"
输出：true
解释：学生缺勤次数少于 2 次，且不存在 3 天或以上的连续迟到记录。

示例 2：
输入：s = "PPALLL"
输出：false
解释：学生最后三天连续迟到，所以不满足出勤奖励的条件。

提示：
1 <= s.length <= 1000
s[i] 为 'A'、'L' 或 'P'
'''
'''
def checkRecord(s):
    # 统计A的数量
    count_A = s.count('A')
    # 判断是否有连续3个L
    has_three_L = "LLL" in s

    # A少于2 并且 没有LLL
    if count_A < 2 and not has_three_L:
        return True
    else:
        return False


# 测试示例
print(checkRecord("PPALLP"))  # True
print(checkRecord("PPALLL"))  # False  有连续3个L
print(checkRecord("AAPPP"))  # False  A有2个
'''

'''

5. 题干
将26个英文字母分为了三组。给你一个字符串数组word，判断字符串中的所有字母是否在同一组。只返回所有字母在同一组的字符串。
请注意，字符串中的字母 不区分大小写，相同字母的大小写形式都被视为在同一组。
26个英文字母分组如下：
第一组由字符 "qwertyuiop" 组成。
第二组由字符 "asdfghjkl" 组成。
第三组由字符 "zxcvbnm" 组成。

示例 1：
输入：words = ["Hello","Alaska","Dad","Peace"]
输出：["Alaska","Dad"]
解释：由于不区分大小写，"a" 和 "A" 都在第二组。

示例 2：
输入：words = ["omk"]
输出：[]

示例 3：
输入：words = ["adsdf","sfd"]
输出：["adsdf","sfd"]

提示：
1 <= words.length <= 20
1 <= words[i].length <= 100
words[i] 由英文字母（小写和大写字母）组成
'''


def findWords(words):
    # 定义三组键盘字母，小写
    line1 = set("qwertyuiop")
    line2 = set("asdfghjkl")
    line3 = set("zxcvbnm")

    res = []
    for word in words:
        # 单词转小写
        w = word.lower()
        # 判断首字符属于哪一行
        if w[0] in line1:
            group = line1
        elif w[0] in line2:
            group = line2
        else:
            group = line3
        # 检查所有字符是否都在本组
        flag = True
        for c in w:
            if c not in group:
                flag = False
                break
        if flag:
            res.append(word)
    return res


# 测试
print(findWords(["Hello", "Alaska", "Dad", "Peace"]))  # ['Alaska', 'Dad']
print(findWords(["omk"]))  # []
print(findWords(["adsdf", "sfd"]))  # ['adsdf', 'sfd']
