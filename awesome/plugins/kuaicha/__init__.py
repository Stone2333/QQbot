from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from .kuaicha import *




__plugin_name__ = '战绩查询'
__plugin_usage__ = r"""
战绩查询格式：
【战绩】+空格+ID
【查战绩】+空格+ID
"""

# 当用户输入关键字没有输入值时则提示
@on_command('kuaicha', aliases=('快查', '快速'), only_to_me=False)
async def kuaicha(session: CommandSession):
    Kuaicha = session.get('Kuaicha', prompt='你想快速查询的类型是?')
    prompt = "查询中请稍候"
    await session.send(prompt)
    qq = session.event['sender']['user_id']
    Overview_report = await kuaicha2(qq, Kuaicha)
    await session.send(Overview_report, at_sender=True)


#  当用户输入关键字和值时直接运行
@kuaicha.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['Kuaicha'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('要查询类型不能为空，请重新输入')

    session.state[session.current_key] = stripped_arg