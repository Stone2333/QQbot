import nonebot
from aiocqhttp.exceptions import Error as CQHttpError
import time
import random
import asyncio

async def qunfa2(message):
    bot = nonebot.get_bot()
    list = await bot.get_group_list()
    for i in list:
        await asyncio.sleep(random.randint(1, 10))
        id = i['group_id']
        if id not in [428422528, 910459586, 458824937]:
            await bot.send_group_msg(group_id=id, message=message)
    return '完成'

