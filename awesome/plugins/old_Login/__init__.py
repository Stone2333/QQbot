from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from .Login_data_source import *
import Mysql_Select, Mysql_Update, Mysql_Insert


# 当用户输入关键字没有输入值时则提示
@on_command('old_Login', aliases=('.旧注册', '.旧注册ID'), only_to_me=False)
async def Login(session: CommandSession):
    try:
        group_id = session.event['group_id']
        number = Mysql_Select.get_statistics_number(group_id, '注册')
        if number:
            Mysql_Update.update_statistics_number(group_id, '注册')
        else:
            Mysql_Insert.insert_statistics_number(group_id, '注册')
    except:
        pass
    Query_Login = session.get('Query_Login', prompt='你想注册ID是多少？')
    Login_report = await get_Login(Query_Login)
    await session.send(Login_report, at_sender=True)


#  当用户输入关键字和值时直接运行
@Login.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['Query_Login'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('要注册的ID不能为空，请重新输入')

    session.state[session.current_key] = stripped_arg