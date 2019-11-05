from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from .Weapons_data_source import *

@on_command('Weapons', aliases=('武器', '查武器'),only_to_me=False)
async def Weapons(session: CommandSession):
    Query_Weapons = session.get('Query_Weapons', prompt='你想查询武器的ID是多少？')
    prompt = "查询中请稍候"
    await session.send(prompt)
    Weapons_report = await get_Weapons(Query_Weapons)
    await session.send(Weapons_report, at_sender=True)


@Weapons.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            session.state['Query_Weapons'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('要查询的ID不能为空，请重新输入')

    session.state[session.current_key] = stripped_arg