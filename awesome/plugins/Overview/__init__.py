from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from .Overview_data_source import *
import Mysql_Select, Mysql_Update, Mysql_Insert



# 当用户输入关键字没有输入值时则提示
@on_command('Overview', aliases=('.旧战绩', '.旧查战绩'), only_to_me=False)
async def Overview(session: CommandSession):
    group_id = session.event['group_id']
    number = Mysql_Select.get_statistics_number(group_id, '战绩')
    if number:
        Mysql_Update.update_statistics_number(group_id, '战绩')
    else:
        Mysql_Insert.insert_statistics_number(group_id, '战绩')
    Query_Overview = session.get('Query_Overview', prompt='你想查询战绩的ID是多少？')
    prompt = "查询中请稍候"
    await session.send(prompt)
    Overview_report = await Select_Overview(Query_Overview)
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