from datetime import datetime

import nonebot
import pytz
from aiocqhttp.exceptions import Error as CQHttpError


# 定时器
@nonebot.scheduler.scheduled_job('cron', hour='*')
async def _():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    try:
        await bot.send_group_msg(group_id=552546607,
                                 message=f'现在{now.hour}点整啦！')
        await bot.send_group_msg(group_id=864770374,
                                 message=f'憨批机器人为您报时现在{now.hour}点整啦！')
    except CQHttpError:
        pass