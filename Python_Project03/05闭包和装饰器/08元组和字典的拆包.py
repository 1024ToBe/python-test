t = (1,5)
d = {'name':'张三','age':22}

def add(x,y):
    print(x+y)
def info(name,age):
    print(f'我{name},{age}岁')

add(*t)      # 拆，作为位置参数传入，等于传入了 3, 5
info(**d)    # 拆，作为关键字参数传入，等于传入了 name="王大锤", age=11