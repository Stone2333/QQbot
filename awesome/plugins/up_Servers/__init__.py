﻿from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from .Servers_data_source import *


@on_command('Servers2', permission=0x0200, aliases=('.up', '.更新服务器'), only_to_me=False)
async def Servers2(session: CommandSession):
    Quer_Servers = session.get('Quer_Servers', prompt='你想更新服务器名称和id？')
    Servers_report = await get_Servers(Quer_Servers)
    await session.send(Servers_report, at_sender=True)


@Servers2.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            session.state['Quer_Servers'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('要查询的服务器名称不能为空，请重新输入')

    session.state[session.current_key] = stripped_arg