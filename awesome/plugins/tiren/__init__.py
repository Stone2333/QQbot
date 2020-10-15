from nonebot import on_command, CommandSession
import nonebot
import re
from aiocqhttp import CQHttp



# 当用户输入关键字没有输入值时则提示
@on_command('Ti',permission=0x0200, aliases=('踢了','ti'), only_to_me=False)
async def Ti(session: CommandSession):
    bot = nonebot.get_bot()
    c = session.event['group_id']
    msg = session.ctx["message"]
    patt = 'qq=(.*)]'
    b = re.findall(pattern=patt, string=str(msg))
    await bot.set_group_kick(group_id=c, user_id=int(b[0]))
