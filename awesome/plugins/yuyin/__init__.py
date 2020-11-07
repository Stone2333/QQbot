from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from .Recent_Sessions_data_source import *



@on_command('yuyin', aliases=('语音'), only_to_me=False)
async def yuyin(session: CommandSession):
    Quer_Recent_Sessions = session.get('Quer_Recent_Sessions', prompt='你想查询最近战绩的ID是多少？')
    Recent_Sessions_report = await get_Recent_Sessions(Quer_Recent_Sessions)
    await session.send(Recent_Sessions_report)


@yuyin.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            session.state['Quer_Recent_Sessions'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('要查询的ID不能为空，请重新输入')

    session.state[session.current_key] = stripped_arg