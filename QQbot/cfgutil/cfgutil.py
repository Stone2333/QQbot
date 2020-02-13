# *-* coding:utf8 *-*
import configparser
import os

# 初始化
config = configparser.ConfigParser()

# 当前目录路径
# dirpath = os.path.dirname(os.path.realpath(__file__))
dirpath = os.path.dirname(os.path.abspath(__file__))
# 项目根路径
rootPath = dirpath[:dirpath.find("QQbot\\") - len("QQbot\\")]  # 获取myProject，也就是项目的根路径
# 配置文件的绝对路径
conf_path = rootPath + "config.ini"
# print(dirpath)
print(conf_path)

# 获取配置项
def getConfig(section: str, key: str, default=""):
    try:
        config.read(conf_path)
        return config.get(section, key)
    except:
        return default


# 设置配置项
def setConfig(section: str, key: str, value: str):
    config.read(conf_path)
    try:
        # 尝试添加配置项，如果有的话就会抛出异常
        config.add_section(section)
    except:
        pass
    config.set(section, key, value)
    config.write(open(conf_path, "r+"))


if __name__ == '__main__':
#     print(getConfig("db", "server"))
#     setConfig("db", "key", "value")
#     setConfig("test", "key", "value")
    pass
