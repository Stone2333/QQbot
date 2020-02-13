# *-* coding:utf8 *-*

import nonebot
from aiocqhttp.exceptions import Error as CQHttpError
from QQbot.awesome.plugins.dingxiang.dingxiang_datasource import *
import time


'''
可选参数
    year=None,
    month=None,
    day=None,
    week=None,
    day_of_week=None,
    hour=None,
    minute=None,
    second=None,
    start_date=None,
    end_date=None,
    timezone=None,
    jitter=None
    
参考文章： https://www.jianshu.com/p/9f0beea09139
'''
# @nonebot.scheduler.scheduled_job('cron',hour='*', minute="*", second="*/4")
# @nonebot.scheduler.scheduled_job('cron',minute="*")
@nonebot.scheduler.scheduled_job('cron',hour="*")
async def _():
    bot = nonebot.get_bot()
    try:
        # await bot.send_group_msg(group_id=552546607,message=queryAll())
        # await bot.send_group_msg(group_id=458824937,message=queryAll())
        # await bot.send_group_msg(group_id=729032552,message=queryAll())
        pass
    except CQHttpError as r:
        print(r)
        pass
