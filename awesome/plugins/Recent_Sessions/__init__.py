from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from .Recent_Sessions_data_source import *

__plugin_name__ = '最近战绩查询'
__plugin_usage__ = r"""最近战绩查询格式：
【最近】+空格+ID
【最近战绩】+空格+ID
【查最近战绩】+空格+ID
"""


@on_command('Recent_Sessions', aliases=('最近', '最近战绩', '查最近战绩'), only_to_me=False)
async def Recent_Sessions(session: CommandSession):
    Quer_Recent_Sessions = session.get('Quer_Recent_Sessions', prompt='你想查询最近战绩的ID是多少？')
    prompt = "查询中稍等片刻"
    await session.send(prompt)
    Recent_Sessions_report = await get_Recent_Sessions(Quer_Recent_Sessions)
    await session.send(Recent_Sessions_report, at_sender=True)


@Recent_Sessions.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            session.state['Quer_Recent_Sessions'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('要查询的ID不能为空，请重新输入')

    session.state[session.current_key] = stripped_arg