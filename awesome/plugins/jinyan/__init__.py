from nonebot import on_command, CommandSession
import nonebot
import re
from aiocqhttp import CQHttp
import Mysql_Select, Mysql_Insert, Mysql_Update


# 当用户输入关键字没有输入值时则提示
@on_command('Jin', permission=0x0200, aliases=('禁言', 'jin'), only_to_me=False)
async def Jin(session: CommandSession):
    bot = nonebot.get_bot()
    group_id = session.event['group_id']
    number = Mysql_Select.get_statistics_number(group_id, '禁言')
    if number:
        Mysql_Update.update_statistics_number(group_id, '禁言')
    else:
        Mysql_Insert.insert_statistics_number(group_id, '禁言')
    msg = session.ctx["message"]
    patt = 'qq=(.*)]'
    b = re.findall(pattern=patt, string=str(msg))

    if b == []:
    # if d == []:
        patt = ' 全体'
        d = re.findall(pattern=patt, string=str(msg))
        patt1 = ' 解除全体'
        k = re.findall(pattern=patt1, string=str(msg))
        if d == [' 全体']:
            await bot.set_group_whole_ban(group_id=group_id, enable=True)
        elif k == [' 解除全体']:
            await bot.set_group_whole_ban(group_id=group_id, enable=False)

    else:
        patt = '](.*)'
        d = re.findall(pattern=patt, string=str(msg))
        print(d)
        if d[0] == ' 解除':
            f = 0
            await bot.set_group_ban(group_id=group_id, user_id=int(b[0]), duration=f)
        elif d == ['']:
            n = 1 * 60
            await bot.set_group_ban(group_id=group_id, user_id=int(b[0]), duration=n)
        else:
            patt = ' \d+'
            k = re.findall(pattern=patt, string=str(msg))
            g = int(k[0]) * 60
            await bot.set_group_ban(group_id=group_id, user_id=int(b[0]), duration=g)
