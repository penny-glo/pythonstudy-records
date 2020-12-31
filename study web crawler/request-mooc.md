12.31 request库
=======

[Request库官网](http://www.python-requests.org)

[Requests Documentation](https://requests.readthedocs.io/_/downloads/en/master/pdf/)

```python
pip install requests

requests.requests()
```

**GET方法**
---
```python
r=requests.get('url',params=none,**kwargs)
```

>reponse对象：爬虫返回的全部内容
  
  ```python
  
  r.status_code        'HTTP请求的返回状态，200表示成功，404表示失败
  
  r.text         'url内容
  
  r.encoding         '网页内容编码方式（从HTTPheader中分析）
  
  r.apparent_encoding         '从内容中分析出相应内容编码方式
  
  r.content        'HTTP相应内容的二进制形式
  ```
  
  ```
  r.apparent_encoding
  r.encoding='  '
  r.text
  
  ```
  
>Requests库的异常
```python
requests.ConnectionError        '网络连接错误异常

requests.HTTPError        'HTTP错误异常

requests.URLRequired        'URL缺失异常

requests.TooManyRedirects        '超过最大重定向次数

requests.ConnectTimeout       '链接远程服务器超时异常

requests.Timeout        '请求URL超时
```

>爬取网页的通用代码框架
```python
import requests

def getHTML.Text(url):
  try:
    r=requests.get(url,timeout=30)
    r.raise_for_status()        '异常处理语句，输出HTTPError
    r.encoding=r.apparent_encoding
    return r.text
  except:
    return "产生异常"
    
if __name__=="__main__":
  url="http://www.baidu.com"
  print(getHTMLText(url))
```
HTTP协议
URL格式：http://host[:post][path]

REQUEST方法
---
```python
requests.request(method,url,**kwargs)
```
>kwargs:控制访问的参数（12个）

HEAD方法
---
获取头部信息
```python
requests.request(url,**kwargs)
```

POST方法
---
在URL位置的资源后增加新的信息
```python
requests.request(url,data=None,json=None,**kwargs)
```

PUT方法
---
在URL位置储存资源，覆盖原有的资源
```python
requests.request(url,data=None,**kwargs)
```

PATCH方法
---
局部更新URL位置的资源
```python
requests.request(url,data=None,**kwargs)
```

DELETE爬虫
---
删除URL位置的资源
```python
requests.request(url,**kwargs)
```

实战案例
---
>案例1：京东商品页面爬取
```python
import requests
url="http://item.jd.com/2967929.html"
try:
  r=requests.get(url)
  r.raise_for_status()
  r.encoding=r.apparent_encoding
  print(r.text[:1000])
except:
  print("爬取失败")
```

>案例2：亚马逊商品页面爬取
r.request.headers 寻找错误原因
```python
import requests
url="http://www.amazon.cn/gp/product/B01M8L5Z3Y"
try:
    kv={'user-agent':'Mozilla/5.0'}
    r=requests.get(url,headers=kv)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(r.text[:1000])
except:
    print("爬取失败")
```

>案例3：百度/360搜索关键词提交
百度关键词接口：http://www.baidu.com/s?wd=keyword
```python
import requests
keyword='python'
try:
    kv={'wd':keyword}
    r=requests.get('http://www.baidu.com/s',params=kv)
    print(r.requests.url)
    r.raise_for_status()
    print(len(r.txt)
except:
    print("爬取失败")
```
