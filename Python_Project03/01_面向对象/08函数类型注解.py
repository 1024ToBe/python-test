
from __future__ import annotations
from typing import Union
def func(a:int,b:str)->int:
    return a+str(b)

#union 联合类型
#列表中元素是字符和数值联合混装
lst: list[Union[str,int]] = [10,'hello',20]
#字典中 value 是字符串和数值混合
dic: dict[str:Union[str,int]] = {'name':'张三','age':22}

#def sum(a: Union[float,int],b: Union[float,int])-> int | float:
    #`int | float` 这种**竖线联合类型**，是 Python3.10 才正式支持的新语法。
    #其他版本要from __future__ import annotations
def sum(a: Union[float, int], b: Union[float, int]) -> Union[float, int]:
    return a+b

ssl = sum(10,12.0)
print(ssl)