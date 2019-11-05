from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from .Overview_data_source import *
# import Mysql_Insert


__plugin_name__ = '战绩查询'
__plugin_usage__ = r"""
战绩查询格式：
【战绩】+空格+ID
【查战绩】+空格+ID
"""

# 当用户输入关键字没有输入值时则提示
@on_command('Overview', aliases=('战绩', '查战绩'), only_to_me=False)
async def Overview(session: CommandSession):
    Query_Overview = session.get('Query_Overview', prompt='你想查询战绩的ID是多少？')
    # await Mysql_Insert.Insert_user(Query_Overview)
    prompt = "查询中请稍候"
    await session.send(prompt)
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