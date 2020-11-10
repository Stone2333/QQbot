from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from .bangding import *
import Mysql_Insert, Mysql_Update, Mysql_Select


@on_command('bangding', aliases=('.bangding', '绑定'), only_to_me=False)
async def bangding(session: CommandSession):
    group_id = session.event['group_id']
    number = Mysql_Select.get_statistics_number(group_id, '绑定')
    if number:
        Mysql_Update.update_statistics_number(group_id, '绑定')
    else:
        Mysql_Insert.insert_statistics_number(group_id, '绑定')
    Bangding = session.get('Bangding', prompt='想要绑定的游戏ID？')
    # prompt = "查询中稍等片刻"
    # await session.send(prompt)
    qq = session.event['sender']['user_id']
    px_name_select_report = await bangding2(Bangding, qq)
    await session.send(px_name_select_report)



@bangding.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            session.state['Bangding'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('想要绑定ID不能为空，请重新输入')

    session.state[session.current_key] = stripped_arg