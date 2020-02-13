# *-* coding:utf8 *-*

# 使用这个工具文件，可以直接生成model对象
import os
from QQbot.cfgutil.cfgutil import getConfig


db_addr = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4".format(
    getConfig("db","username"),
    getConfig("db","password"),
    getConfig("db","server"),
    getConfig("db","port"),
    getConfig("db","database")
)

os.system('sqlacodegen "{}" > model/model.py'.format(db_addr))
print("生成模型完成")