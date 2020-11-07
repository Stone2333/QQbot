from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from .Servers_data_source import *


@on_command('Servers', aliases=('服务器', '查服务器'),only_to_me=False)
async def Servers(session: CommandSession):
    Quer_Servers = session.get('Quer_Servers', prompt='你想查询服务器名称是多少？')
    prompt = "查询中稍等片刻"
    await session.send(prompt)
    Servers_report = await get_Servers(Quer_Servers)
    await session.send(Servers_report, at_sender=True)


@Servers.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            session.state['Quer_Servers'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('要查询的服务器名称不能为空，请重新输入')

    session.state[session.current_key] = stripped_arg