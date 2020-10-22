from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from .bangding import *


@on_command('bangding', aliases=('.bangding', '绑定'), only_to_me=False)
async def bangding(session: CommandSession):
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