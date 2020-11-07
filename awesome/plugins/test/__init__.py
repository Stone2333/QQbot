from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from .Login_data_source import *


__plugin_name__ = '注册'
__plugin_usage__ = r"""
注册查询格式：
【注册】+空格+ID
"""

# 当用户输入关键字没有输入值时则提示
@on_command('test', patterns=('.最近','.武器','.载具','.战绩','快速链接','劳动仲裁'), only_to_me=False)
async def test(session: CommandSession):
    test1 = session.get('test1', prompt='你想注册ID是多少？')
    qq = session.event['sender']['user_id']
    img = await get_img(qq, test1, session)
    await session.send(img, at_sender=True)


#  当用户输入关键字和值时直接运行
@test.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['test1'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('要注册的ID不能为空，请重新输入')

    session.state[session.current_key] = stripped_arg