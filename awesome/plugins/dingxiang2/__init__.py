from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from .dinxiangchaxun2 import *
import Mysql_Select, Mysql_Update, Mysql_Insert



# 当用户输入关键字没有输入值时则提示
@on_command('cha1', aliases=('疫情详细', '疫情'), only_to_me=False)
async def cha1(session: CommandSession):
    try:
        group_id = session.event['group_id']
        number = Mysql_Select.get_statistics_number(group_id, '疫情')
        if number:
            Mysql_Update.update_statistics_number(group_id, '疫情')
        else:
            Mysql_Insert.insert_statistics_number(group_id, '疫情')
    except:
        pass
    Query_Login = session.get('chaxun1', prompt='请输入"全国"')
    chaxun = await dingxiang(Query_Login)
    await session.send(chaxun)


#  当用户输入关键字和值时直接运行
@cha1.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['chaxun1'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('请输入"全国"，请重新输入')

    session.state[session.current_key] = stripped_arg