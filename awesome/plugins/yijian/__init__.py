from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from .yijian import *


@on_command('yijian', aliases=('.yijian', '意见'), only_to_me=False)
async def yijian(session: CommandSession):
    Yijian = session.get('Yijian', prompt='你想提的意见？')
    # prompt = "查询中稍等片刻"
    # await session.send(prompt)
    qq = session.event['sender']['user_id']
    px_name_select_report = await yijian2(Yijian, qq)
    await session.send(px_name_select_report)



@yijian.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            session.state['Yijian'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('要查询的ID不能为空，请重新输入')

    session.state[session.current_key] = stripped_arg