12.29 Beautiful Soup
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
|Name|<tag>.name|
|Attributes|<tag>.attrs（字典）|
|NavigableString|<tag>.string|
|Comment|注释|

