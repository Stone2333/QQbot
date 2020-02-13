import nonebot
import config
from os import path

if __name__ == '__main__':
    nonebot.init(config)
    nonebot.load_plugins(
        path.join(path.dirname(__file__), 'awesome', 'plugins'),
        'awesome.plugins'
    )
    # 这里添加参数是因为在mac环境无法启动，通过官方QQ群询问群主得到的临时解决方案
    # nonebot.run()
    nonebot.run(use_reloader=False)
