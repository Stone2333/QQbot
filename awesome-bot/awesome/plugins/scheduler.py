from datetime import datetime

import nonebot
import pytz
from aiocqhttp.exceptions import Error as CQHttpError


# 定时器
@nonebot.scheduler.scheduled_job('interval', minutes=10)
async def _():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    try:
        await bot.send_group_msg(group_id=552546607,
                                 message=f'现在为你播报')
        await bot.send_group_msg(group_id=864770374,
                                 message=f'憨批机器人为您嘴臭:NMSL')
        await bot.send_group_msg(group_id=729032552,
                                 message=f'憨批机器人为您嘴臭:NMSL')
    except CQHttpError:
        pass