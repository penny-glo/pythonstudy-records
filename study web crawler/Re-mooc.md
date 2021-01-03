1.1 Re
===
正则表达式
---
正则表达式（RE）：简洁表达一组字符串的表达式

[正则表达式HOWTO](https://docs.python.org/zh-cn/3/howto/regex.html#regex-howto)

功能函数
---
import re

re.search()   搜索匹配正则表达式的第一个位置
```python
re.search(pattern,string,flag=0)
```
>pattern：正则表达式字符串或原生字符串

>string：待匹配字符串

>flags：控制标记

>>re.I   忽略大小写

>>re.M   匹配每行

>>re.S   .操作符匹配所有字符

re.match()    在字符串开始位置匹配正则表达式

re.findall()    以列表类型返回全部能匹配的子串

re.split()    将一个字符串按正则表达式类型进行分割，返回列表类型

re.finditer()   返回匹配结果的迭代类型

re.sub()    替换所有匹配正则表达式的字符串

匹配方式
---
贪婪匹配（默认）：输出最长的表达式

最小匹配：输出最短的表达式

match=re.search(r'PY.*?N','PYANBNCNDN')

*?  +?  ??  {m,n}?
