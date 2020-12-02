from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from .Login_data_source import *
import Mysql_Insert, Mysql_Update, Mysql_Select


# 当用户输入关键字没有输入值时则提示
@on_command('kuaicha', patterns=('^.最近$','^.武器$','^.载具$','^.战绩$','^帮助$','快速链接'), only_to_me=False)
async def kuaicha(session: CommandSession):
    try:
        group_id = session.event['group_id']
        number = Mysql_Select.get_statistics_number(group_id, '快速查询')
        if number:
            Mysql_Update.update_statistics_number(group_id, '快速查询')
        else:
            Mysql_Insert.insert_statistics_number(group_id, '快速查询')
    except:
        pass
    test1 = session.get('test1', prompt='你想？')
    qq = session.event['sender']['user_id']
    img = await get_img(qq, test1, session)
    await session.send(img, at_sender=True)


#  当用户输入关键字和值时直接运行
@kuaicha.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['test1'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('要注册的ID不能为空，请重新输入')

    session.state[session.current_key] = stripped_arg