from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from .Servers_data_source import *
import Mysql_Insert, Mysql_Update, Mysql_Select


@on_command('Servers1', permission=0x0200, aliases=('.in', '.新增服务器'), only_to_me=False)
async def Servers1(session: CommandSession):
    try:
        group_id = session.event['group_id']
        number = Mysql_Select.get_statistics_number(group_id, '新增服务器')
        if number:
            Mysql_Update.update_statistics_number(group_id, '新增服务器')
        else:
            Mysql_Insert.insert_statistics_number(group_id, '新增服务器')
    except:
        pass
    Quer_Servers = session.get('Quer_Servers', prompt='你想查询服务器名称是多少？')
    Servers_report = await get_Servers(Quer_Servers)
    await session.send(Servers_report, at_sender=True)


@Servers1.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            session.state['Quer_Servers'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('要查询的服务器名称不能为空，请重新输入')

    session.state[session.current_key] = stripped_arg