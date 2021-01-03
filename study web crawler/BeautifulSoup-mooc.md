12.31 Beautiful Soup
===
[Beautiful Soup中文文档](https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/)

[Beautiful Soup文档下载](https://readthedocs.org/projects/beautiful-soup-4/downloads/pdf/latest/)

基本代码
---
```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(<p> data </p>, 'html.parser')
```
>解析器

|解析器|使用方法|安装条件|
|---|---|---|
|bs4的HTML解析器|BeautifulSoup(markup,'html.parser')|安装bs4|
|lxml的HTML解析器|BeautifulSoup(markup, "lxml")|pip install lxml|
|lxml的XML解析器|BeautifulSoup(markup, "xml")|pip install lxml|
|html5lib解析器|BeautifulSoup(markup, "html5lib")|pip install l5lib|

>基本元素

|元素|使用方式|
|---|---|
|Tag|<>……</>|
|Name|<t>.name|
|Attributes|<t>.attrs（字典）|
|NavigableString|<t>.string|
|Comment|注释|

#tag
```python
tag=soup.<tag>
```

#name
```python
soup.a.name
```

#attributes
```python
tag=soup.a
tag.attrs
tag.attrs['class']
typr(tag.attrs)
```

#string
```python
soup.a.string
```

#comment
```python
>>>type(soup.p.string)
<class 'bs4.element.NavigableString'>
```

>标签树的遍历
>>下行遍历
.contents 将tag的子节点以列表的方式输出

.children 遍历所有子节点

.decendants 循环遍历所有子孙节点

>>上行遍历
.parent 节点父标签

.parents 遍历先辈节点

>>平行遍历
.next_sibling

.previous_sibling

.next_siblings

.previous_siblings

>美化页面
soup.prettify() 增加换行符

>信息提取
```python
soup.find_all(name,attrs,recursive,string,**kwargs)
```

实战案例：中国大学排名
---
http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html
https://www.shanghairanking.cn/rankings/bcur/2020
