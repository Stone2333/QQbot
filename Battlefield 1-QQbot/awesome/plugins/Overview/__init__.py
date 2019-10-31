from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from jieba import posseg
from .Overview_data_source import *

# 当用户输入关键字没有输入值时则提示
@on_command('Overview', aliases=('战绩', '查战绩'), only_to_me=False)
async def Overview(session: CommandSession):
    Query_Overview = session.get('Query_Overview', prompt='你想查询战绩的ID是多少？')
    a = "查询中请稍候"
    await session.send(a)
    Overview_report = await get_Overview(Query_Overview)
    await session.send(Overview_report, at_sender=True)


#  当用户输入关键字和值时直接运行
@Overview.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['Query_Overview'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('要查询的ID不能为空，请重新输入')

    session.state[session.current_key] = stripped_arg