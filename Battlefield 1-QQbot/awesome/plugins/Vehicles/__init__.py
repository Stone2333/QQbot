from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from jieba import posseg
from .Vehicles_data_source import *


@on_command('Vehicles', aliases=('载具', '查载具'),only_to_me=False)
async def Vehicles(session: CommandSession):
    Query_Vehicles = session.get('Query_Vehicles', prompt='你想查询载具的ID是多少？')
    a = "查询中稍等片刻"
    await session.send(a)
    Vehicles_report = await get_Vehicles(Query_Vehicles)
    await session.send(Vehicles_report, at_sender=True)


@Vehicles.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            session.state['Query_Vehicles'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('要查询的ID不能为空，请重新输入')

    session.state[session.current_key] = stripped_arg