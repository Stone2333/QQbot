from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand





# 当用户输入关键字没有输入值时则提示
@on_command('kuaicha2', patterns='快速链接', only_to_me=False)
async def kuaicha2(session: CommandSession):
    msg = """
    https://www.ceve-market.org/index/
    """
    await session.send(msg)