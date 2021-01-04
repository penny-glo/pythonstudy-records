[Python Documentation中文版](https://docs.python.org/zh-cn/3/tutorial/classes.html)

```python

#类用单词首字母大写命名（如CourtFromBy），函数用小写字母与下划线强调（如court_from_by）
class CountFromBy:

    #'object'类覆盖'__init__'方法，用于初始化
    def __init__(self,v:int,i:int) -> None:
        self.val = v
        self.incr = i
        
    #每一个函数的第一个参数为self
    def increase(self) -> None:
        self.val += self.incr
    
    #返回对象以标准字符串表示
    def __repr__(self) -> str:
        return str(self.val)
        
```
