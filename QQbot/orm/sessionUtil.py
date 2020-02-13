# *-* coding:utf8 *-*
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from QQbot.cfgutil.cfgutil import getConfig
from QQbot.orm.model.model import *
import time

Base = declarative_base()
# 连接数据库
# engine = create_engine("mysql+pymysql://root:root@127.0.0.1:3306/qq_bot?charset=utf8mb4")
engine = create_engine("mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4".format(
    getConfig("db","username"),
    getConfig("db","password"),
    getConfig("db","server"),
    getConfig("db","port"),
    getConfig("db","database")
))

session = sessionmaker(engine)
mySession = session()

def now():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

if __name__ == '__main__':
    print(mySession.query(User).count())