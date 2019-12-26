# BF1_QQbot
NoneBot 是一个基于 酷Q 的 Python 异步 QQ 机器人框架，它会对 QQ 机器人收到的消息进行解析和处理，并以插件化的形式，分发给消息所对应的命令处理器和自然语言处理器，来完成具体的功能。  

除了起到解析消息的作用，NoneBot 还为插件提供了大量实用的预设操作和权限控制机制，尤其对于命令处理器，它更是提供了完善且易用的会话机制和内部调用机制，以分别适应命令的连续交互和插件内部功能复用等需求。  

NoneBot 在其底层与 酷Q 交互的部分使用 python-aiocqhttp 库，后者是 CoolQ HTTP API 插件 的一个 Python 异步 SDK，在 Quart 的基础上封装了与 CoolQ HTTP API 插件的网络交互。  

得益于 Python 的 asyncio 机制，NoneBot 处理消息的吞吐量有了很大的保障，再配合 CoolQ HTTP API 插件可选的 WebSocket 通信方式（也是最建议的通信方式），NoneBot 的性能可以达到 HTTP 通信方式的两倍以上，相较于传统同步 I/O 的 HTTP 通信，更是有质的飞跃。  


# 机器人能做什么
查询服务器状态:
关键字：服务器，查服务器  
方法1（关键字带值）：关键字+空格+游戏ID   
方法2（关键字不带值）：发送关键字后会提示，输入需要查询的服务器名称即可  

查询个人游戏战绩：   
关键字：战绩，查战绩   
方法1（关键字带值）：关键字+空格+游戏ID   
方法2（关键字不带值）：发送关键字后会提示，输入需要查询的游戏ID即可  

查询个人武器数据：  
关键字：武器，查武器  
方法1（关键字带值）：关键字+空格+游戏ID   
方法2（关键字不带值）：发送关键字后会提示，输入需要查询的游戏ID即可 

查询个人载具数据：  
关键字：载具，查载具   
方法1（关键字带值）：关键字+空格+游戏ID   
方法2（关键字不带值）：发送关键字后会提示，输入需要查询的游戏ID即可 

查询个人最近游戏数据：  
关键字：最近，最近战绩，查最近战绩    
方法1（关键字带值）：关键字+空格+游戏ID   
方法2（关键字不带值）：发送关键字后会提示，输入需要查询的游戏ID即可  

注册ID：  
关键字：注册，注册ID 
方法1（关键字带值）：关键字+空格+游戏ID   
方法2（关键字不带值）：发送关键字后会提示，输入需要注册游戏ID即可 

# 注意：是否注册不影响查询，但会影响战绩、载具、武器数据更新！！！

# 待完成
数据库表结构设计  （完成）  
将获取到的ID和所爬取的信息存到数据库  （完成）  
实现定时任务每天十二点触发全库爬取  （完成）  
实现数据库查询数据，提高查询速度，解决服务器延迟问题和网站挂掉无法提供服务的问题  （完成）  
时效性较高的信息需要实时爬取展示  （完成）  
更新数据sql语句忘了写！！！（完成）
优化爬虫代码
寻找潜在BUG




