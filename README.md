# QQbot
QQbot是使用[NoneBot](https://nonebot.cqp.moe/)的异步QQ机器人框架所完成。

### 机器人能做什么
- 战地1战绩信息查询
  - 个人总战绩查询
  - 个人武器数据查询
  - 个人载具信息查询
  - 个人最近战绩信息查询
  - 服务器信息查询

- 成都培训机构查询
  - 根据名字查询培训机构
  - 根据地址查询培训机构
  - 插入培训新信息

### 环境部署
具体部署环境不再陈述，请按照以下安装指南部署环境[NoneBot安装指南](https://nonebot.cqp.moe/guide/)
并安装对应[依赖包](https://github.com/Stone2333/BF1_QQbot/blob/master/Pipfile.txt)。

### 任务
- [x] 已完成
  - [x] 将获取到的游戏名称和所爬取的信息存到数据库。
  - [x] 实现数据库查询数据，提高查询速度，解决服务器延迟问题和网站挂掉无法提供服务的问题。
  - [x] 实现定时任务每天十二点，根据注册表获取游戏名称全库更新。
  - [x] 时效性较高的信息需实时爬取展示，不做数据库存储。
 
- [ ] 未完成 
  - [ ] 战地数据库表结构重新设计。 
  - [ ] 培训机构数据爬虫定时任务新增和更新。
  - [ ] 战地1爬虫代码优化。

### 贡献
如果在使用中发现任何问题，可以[提交问题](https://github.com/Stone2333/BF1_QQbot/issues/new)


