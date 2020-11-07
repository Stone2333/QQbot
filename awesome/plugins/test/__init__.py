from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from .Login_data_source import *


__plugin_name__ = '注册'
__plugin_usage__ = r"""
注册查询格式：
【注册】+空格+ID
"""

# 当用户输入关键字没有输入值时则提示
@on_command('test', patterns=('色图','吃瓜','劳动仲裁'), only_to_me=False)
async def test(session: CommandSession):
    img = await get_img(str(session))
    await session.send(img)