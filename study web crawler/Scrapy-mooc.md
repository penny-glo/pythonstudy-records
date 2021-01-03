# 1.3 Scrapy库（爬虫框架）

[scrapy官网](https://scrapy.org/)

[scrapy documentation](https://docs.scrapy.org/_/downloads/en/latest/pdf/)

[scrapy中文文档](https://scrapy-chs.readthedocs.io/zh_CN/1.0/intro/tutorial.html)

## 框架结构

### Engine

控制所有模块的数据流

根据条件触发事件

### Downloader

根据请求下载网页

### Scheduler

根据请求调度管理

### Spider（可编辑）

解析downloader返回的响应

产生爬取项

产生额外的爬取请求

### Item Pipelines（可编辑）

以流水线处理Spider产生的爬取项

清理，检验，查重，储存到数据库

### Downloader Middleware（可编辑）

修改、丢弃、新增请求和响应

### Spider Middleware（可编辑）

对请求和爬取项的再处理，修改、丢弃、新增请求或爬取项

## 常用命令

'''python
>scrapy<command>[option][args]
'''

>command

|命令|格式|说明|
|---|---|---|
|startproject|scrapy startproject <project_name>|在 project_name 文件夹下创建一个名为 project_name 的Scrapy项目|
|genspider|scrapy genspider [-t template] <name> <domain>|在当前项目中创建爬虫|
|settings|scrapy settings [options]|获取爬虫的设定|
|crawl|scrapy crawl <spider>|运行一个爬虫|
|list|scrapy list|列出所有爬虫|
|shell|scrapy shell [url]|启动URL调试命令行|
