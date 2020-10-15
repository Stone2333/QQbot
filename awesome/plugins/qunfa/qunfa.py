import nonebot
from aiocqhttp.exceptions import Error as CQHttpError


async def qunfa2(message):
    bot = nonebot.get_bot()
    list = await bot.get_group_list()
    try:
        for i in list:
            group = i['group_id']
            if group != 428422528 or 910459586 or 458824937 or 712532013 or 419868786:
                await bot.send_group_msg(group_id=group, message=message)
    except CQHttpError:
        pass