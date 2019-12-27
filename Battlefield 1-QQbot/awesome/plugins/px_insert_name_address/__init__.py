from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from .px_insert_data_source import *


@on_command('px_name_insert', aliases=('插入培训', '培训插入'), only_to_me=False)
async def px_name_insert(session: CommandSession):
    Quer_px_name_insert = session.get('Quer_px_name_insert', prompt='你想插入的培训公司名称地址是什么？用英文逗号分隔')
    # prompt = "查询中稍等片刻"
    # await session.send(prompt)
    px_name_select_report = await get_px_insert(Quer_px_name_insert)
    await session.send(px_name_select_report)


@px_name_insert.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            session.state['Quer_px_name_insert'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('要查询的ID不能为空，请重新输入')

    session.state[session.current_key] = stripped_arg