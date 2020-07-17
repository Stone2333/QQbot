from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from .wuping import *



# 当用户输入关键字没有输入值时则提示
@on_command('wuping', aliases=('价格', '查价格','jita','.jita','物价'), only_to_me=False)
async def wuping(session: CommandSession):
    chawuping = session.get('chawuping', prompt='你想查询的物品名称是什么？')
    wuping = await get_wuping(chawuping)
    await session.send(wuping, at_sender=True)


#  当用户输入关键字和值时直接运行
@wuping.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['chawuping'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('要查询的物品名称不能为空，请重新输入')

    session.state[session.current_key] = stripped_arg