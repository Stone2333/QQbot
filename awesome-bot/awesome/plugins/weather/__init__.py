from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
# from jieba import posseg
from .data_source import *


@on_command('zhanji', aliases=('战绩', '查战绩'), only_to_me=False)
async def zhanji(session: CommandSession):
    chazhanji = session.get('chazhanji', prompt='你想查询战绩的ID是多少？')
    a = "查询中请稍候"
    await session.send(a)
    zhanji_report = await get_zhanji(chazhanji)
    await session.send(zhanji_report, at_sender=True)

@on_command('wuqi', aliases=('武器', '查武器'),only_to_me=False)
async def wuqi(session: CommandSession):
    chawuqi = session.get('chawuqi', prompt='你想查询武器的ID是多少？')
    a = "查询中请稍候"
    await session.send(a)
    wuqi_report = await get_wuqi(chawuqi)
    await session.send(wuqi_report, at_sender=True)

@on_command('zuijinzhanji', aliases=('最近', '最近战绩', '查最近战绩'),only_to_me=False)
async def zuijinzhanji(session: CommandSession):
    chazuijinzhanji = session.get('chazuijinzhanji', prompt='你想查询最近战绩的ID是多少？')
    a = "查询中稍等片刻"
    await session.send(a)
    zuijinzhanji_report = await get_zuijinzhanji(chazuijinzhanji)
    await session.send(zuijinzhanji_report, at_sender=True)

@on_command('fuwuqi', aliases=('服务器', '查服务器'),only_to_me=False)
async def fuwuqi(session: CommandSession):
    chafuwuqi = session.get('chafuwuqi', prompt='你想查询服务器名称是多少？')
    a = "查询中稍等片刻"
    await session.send(a)
    fuwuqi_report = await get_fuwuqi(chafuwuqi)
    await session.send(fuwuqi_report, at_sender=True)

@on_command('zaiju', aliases=('载具', '查载具'),only_to_me=False)
async def zaiju(session: CommandSession):
    chazaiju = session.get('chazaiju', prompt='你想查询载具的ID是多少？')
    a = "查询中稍等片刻"
    await session.send(a)
    zaiju_report = await get_zaiju(chazaiju)
    await session.send(zaiju_report, at_sender=True)

@zhanji.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['chazhanji'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('要查询的ID不能为空，请重新输入')

    session.state[session.current_key] = stripped_arg


@wuqi.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        # 该命令第一次运行（第一次进入命令会话）
        if stripped_arg:
            session.state['chawuqi'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('要查询的ID不能为空，请重新输入')

    session.state[session.current_key] = stripped_arg


@zuijinzhanji.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            session.state['chazuijinzhanji'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('要查询的ID不能为空，请重新输入')

    session.state[session.current_key] = stripped_arg

@fuwuqi.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            session.state['chafuwuqi'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('要查询的服务器名称不能为空，请重新输入')

    session.state[session.current_key] = stripped_arg

@zaiju.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            session.state['chazaiju'] = stripped_arg
        return
    
    if not stripped_arg:
        session.pause('要查询的ID不能为空，请重新输入')

    session.state[session.current_key] = stripped_arg
    
    
# 模糊搜索模块
# on_natural_language 装饰器将函数声明为一个自然语言处理器
# keywords 表示需要响应的关键词，类型为任意可迭代对象，元素类型为 str
# # 如果不传入 keywords，则响应所有没有被当作命令处理的消息
# @on_natural_language(keywords={'战绩', '查战绩'}, only_to_me=False)
# async def _(session: NLPSession):
#
#     return IntentCommand(90.0, 'zhanji')
#
# @on_natural_language(keywords={'武器', '查武器'}, only_to_me=False)
# async def _(session: NLPSession):
#
#     return IntentCommand(90.0, 'wuqi')
#
# @on_natural_language(keywords={'最近', '最近战绩', '查最近战绩'}, only_to_me=False)
# async def _(session: NLPSession):
#     # 返回意图命令，前两个参数必填，分别表示置信度和意图命令名
#     return IntentCommand(90.0, 'chazuijinzhanji')
#
# @on_natural_language(keywords={'服务器', '查服务器'}, only_to_me=False)
# async def _(session: NLPSession):
#     # 返回意图命令，前两个参数必填，分别表示置信度和意图命令名
#     return IntentCommand(90.0, 'fuwuqi')
#
# @on_natural_language(keywords={'载具', '查载具'}, only_to_me=False)
# async def _(session: NLPSession):
#     # 返回意图命令，前两个参数必填，分别表示置信度和意图命令名
#     return IntentCommand(90.0, 'zaiju')
#
#
# @on_natural_language(keywords={'天气'}, only_to_me=False)
# async def _(session: NLPSession):
#     # 返回意图命令，前两个参数必填，分别表示置信度和意图命令名
#     return IntentCommand(90.0, 'weather')

