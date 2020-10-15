from nonebot import on_command, CommandSession
import nonebot
import re
from aiocqhttp import CQHttp



# 当用户输入关键字没有输入值时则提示
@on_command('Jin', permission=0x0200, aliases=('禁言', 'jin'), only_to_me=False)
async def Jin(session: CommandSession):
    bot = nonebot.get_bot()
    c = session.event['group_id']
    msg = session.ctx["message"]
    patt = 'qq=(.*)]'
    b = re.findall(pattern=patt, string=str(msg))
    patt = ' ,(.*)'
    d = re.findall(pattern=patt, string=str(msg))
    if d == []:
        patt = ' 全体'
        d = re.findall(pattern=patt, string=str(msg))
        patt1 = ' 解除全体'
        k = re.findall(pattern=patt1, string=str(msg))
        if d == [' 全部']:
            await bot.set_group_whole_ban(group_id=c, enable=True)
        elif k == [' 解除全体']:
            await bot.set_group_whole_ban(group_id=c, enable=False)
    else:
        if d[0] == '解除':
            f = 0
            await bot.set_group_ban(group_id=c, user_id=int(b[0]), duration=f)
        else:
            g = int(d[0]) * 60
            await bot.set_group_ban(group_id=c, user_id=int(b[0]), duration=g)
