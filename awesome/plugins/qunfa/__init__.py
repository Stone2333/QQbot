from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from .qunfa import *


@on_command('qunfa', aliases=('.qun', '.qunfa'), only_to_me=False)
async def qunfa(session: CommandSession):
    Qunfa = session.get('Qunfa', prompt='你想群发的？')
    # prompt = "查询中稍等片刻"
    # await session.send(prompt)
    px_name_select_report = await qunfa2(Qunfa)
    await session.send('完成')


@qunfa.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            session.state['Qunfa'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('要查询的ID不能为空，请重新输入')

    session.state[session.current_key] = stripped_arg