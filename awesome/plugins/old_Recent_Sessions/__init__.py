from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from .Recent_Sessions_data_source import *
import Mysql_Insert, Mysql_Update, Mysql_Select


@on_command('old_Recent_Sessions', aliases=('.旧最近'), only_to_me=False)
async def Recent_Sessions(session: CommandSession):
    group_id = session.event['group_id']
    number = Mysql_Select.get_statistics_number(group_id, '旧最近战绩')
    if number:
        Mysql_Update.update_statistics_number(group_id, '旧最近战绩')
    else:
        Mysql_Insert.insert_statistics_number(group_id, '旧最近战绩')
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