from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from .px_name_data_source import *


@on_command('px_name_select', aliases=('培训名称', '查培训名称', '培训查询', '查询培训', '培训名字', '是不是培训'), only_to_me=False)
async def px_name_select(session: CommandSession):
    Quer_px_name_select = session.get('Quer_px_name_select', prompt='你想查询是否培训公司的名称是什么？')
    # prompt = "查询中稍等片刻"
    # await session.send(prompt)
    px_name_select_report = await get_px_name_select(Quer_px_name_select)
    print(px_name_select_report)
    await session.send(px_name_select_report)


@px_name_select.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            session.state['Quer_px_name_select'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('要查询的ID不能为空，请重新输入')

    session.state[session.current_key] = stripped_arg