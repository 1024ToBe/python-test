class Dog():
    # 1.对象被创建时调用
    def __init__(self,name,color,age,height,friends):
        self.name = name
        self.color = color
        self.age = age
        self.height = height
        self.friends = friends

    #2.打印对象信息时不再默认打印地址，而是打印自定义内容
    def __str__(self):
        str = f'我是{self.name}狗子，颜色{self.color},今年{self.age},体重{self.height},我的好朋友是{self.friends}」'
        return str

    #3.对象被销毁时调用
    def __del__(self):
        print(f'{self.name}狗子 已被收回')


    #4.下标取值 `obj[0]`
    def __getitem__(self, item):
        return self.friends[0]

    '''
方法	  运算符	英文	               含义
__lt__	<	less than	       小于
__le__	<=	less or equal	   小于等于
__gt__	>	greater than	   大于
__ge__	>=	greater or equal   大于等于
__eq__	==	equal	           等于
__ne__	!=	not equal	       不等于
    '''
    # gt:大于, >, greater than
    # ge：大于等于, >=, greater or equal
    def __gt__(self, other):
        # self > other，按年龄比较
        return self.age > other.age

    # lt:,小于, <, less than
    # le:小于等于，<=, less or equal
    def __lt__(self, other):
        return self.age < other.age

    # == 等于 equal
    #__ne__:!=,not equal,不等于
    def __eq__(self, other):
        return self.age == other.age




d1 = Dog('废柴','黑色','3', 10,['小黑','小白','小花'])
print(d1)
#多1个引用
d2 = d1
#引用计数不是0 所以不会被销毁
#del d1
print('------------------')
#引用计数=0 被销毁
#del d2

d11 = Dog('旺仔','白色','5', 12,['小浪','小米','小灰'])
print(d11[0])
# 代码运行全部结束后，解释器回收对象，触发 __del__，d11被收回
print('旺仔比废柴年龄大吗?',d11.__gt__(d1))




