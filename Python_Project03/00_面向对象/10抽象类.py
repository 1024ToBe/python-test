'''
抽象类：不能实例化（不能 new 对象），里面包含抽象方法（只有方法声明，没有具体实现），用来强制子类必须重写这个方法。
抽象类本身是【模板、规范】，只规定 “子类必须有哪些方法”，不做具体实现。
抽象方法：用 `@abstractmethod` 装饰，只有 def 定义，没有代码逻辑（pass）

Python 需要导入模块：`from abc import ABC, abstractmethod`
- ABC：Abstract Base Class，抽象基类（用来做父类，变成抽象类）
- @abstractmethod：抽象方法装饰器

from abc import ABC, abstractmethod

class 抽象类(ABC):
    @abstractmethod
    def 方法(self, ...) -> xxx:
        pass
'''

from abc import ABC,abstractmethod
class ABCFileService(ABC):
    @abstractmethod
    def read_oneline(self)->str:
        pass

    @abstractmethod
    def write_oneline(self,context:str) -> bool:
        pass

    @abstractmethod
    def print_all(self,context:str) -> None:
        pass

    @abstractmethod
    def read_all(self) -> str:
        pass

class TextFileService(ABCFileService):
    def __init__(self,file_path):
        self.fr = open(file_path,'r',encoding='utf8')
        self.fw = open(file_path,'a',encoding='utf8')

    def read_oneline(self) -> str:
        self.fr.seek(0)
        return self.fr.readline()

    def write_oneline(self, context: str) -> bool:
        try:
            self.fw.seek(0)
            self.fw.write(context+'\n')
            # self.fw.write('\n')
            # self.fw.flush()
            return True
        except Exception:
            return False

    def print_all(self, context: str) -> None:
        self.fr.seek(0)
        print(self.fr.read())

    def read_all(self) -> str:
        self.fr.seek(0)
        return self.fr.read()

tfs = TextFileService("data.txt")
# tfs.write_oneline("abcde")
# tfs.write_oneline("啦啦啦啦啦")
print(tfs.read_oneline())
# print(tfs.read_all())