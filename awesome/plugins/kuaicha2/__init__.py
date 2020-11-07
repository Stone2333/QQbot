from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand




@on_command('kuaicha2', patterns=[r'快速链接'], only_to_me=False)
async def kuaicha2(session: CommandSession):
    msg = """
    https://www.ceve-market.org/index/
    """
    await session.send(msg)