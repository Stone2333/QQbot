from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
import Test_data_source

__plugin_name__ = '测试模块'
__plugin_usage__ = r"""
测试模块：
mysql新增，查询，更新
定任务失败重跑
"""

@on_command('Test_Overview', aliases=('测试1', '测试战绩'), only_to_me=False)
async def Test_Overview(session: CommandSession):
    Test_Query_Overview = session.get('Test_Query_Overview', prompt='你想查询战绩的ID是多少？')
    prompt = "查询中请稍候"
    await session.send(prompt)
    print(session)
    Test_Overview_report = await Test_data_source.Tset_Select_Overview(Test_Query_Overview)
    await session.send(Test_Overview_report, at_sender=True)

#  当用户输入关键字和值时直接运行
@Test_Overview.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['Test_Query_Overview'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('要查询的ID不能为空，请重新输入')

    session.state[session.current_key] = stripped_arg


@on_command('Test_Servers_Id', aliases=('测试服务器ID', '测试查服务器ID'),only_to_me=False)
async def Test_Servers_Id(session: CommandSession):
    Test_Quer_Servers = session.get('Test_Quer_Servers_Id', prompt='你想查询服务器名称是多少？')
    prompt = "查询中稍等片刻"
    await session.send(prompt)
    Test_Servers_report = await Test_data_source.Tset_Select_Servers_Id(Test_Quer_Servers)
    await session.send(Test_Servers_report, at_sender=True)


@Test_Servers_Id.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            session.state['Test_Quer_Servers_Id'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('要查询的服务器名称不能为空，请重新输入')

    session.state[session.current_key] = stripped_arg



@on_command('Test_Servers', aliases=('测试服务器', '测试查服务器'),only_to_me=False)
async def Test_Servers(session: CommandSession):
    Test_Quer_Servers = session.get('Test_Quer_Servers', prompt='你想查询服务器名称是多少？')
    prompt = "查询中稍等片刻"
    await session.send(prompt)
    Test_Servers_report = await Test_data_source.Tset_Select_Servers(Test_Quer_Servers)
    await session.send(Test_Servers_report, at_sender=True)


@Test_Servers.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            session.state['Test_Quer_Servers'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('要查询的服务器名称不能为空，请重新输入')

    session.state[session.current_key] = stripped_arg

@on_command('Test_Weapons', aliases=('测试武器', '测试查武器'),only_to_me=False)
async def Test_Weapons(session: CommandSession):
    Test_Query_Weapons = session.get('Test_Query_Weapons', prompt='你想查询武器的ID是多少？')
    prompt = "查询中请稍候"
    await session.send(prompt)
    Test_Weapons_report = await Test_data_source.Tset_Select_Weapons(Test_Query_Weapons)
    await session.send(Test_Weapons_report, at_sender=True)

@Test_Weapons.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            session.state['Test_Query_Weapons'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('要查询的ID不能为空，请重新输入')

    session.state[session.current_key] = stripped_arg


@on_command('Test_Recent_Sessions', aliases=('测试最近', '测试最近战绩', '测试最近战绩'), only_to_me=False)
async def Test_Recent_Sessions(session: CommandSession):
    Test_Quer_Recent_Sessions = session.get('Test_Quer_Recent_Sessions', prompt='你想查询最近战绩的ID是多少？')
    prompt = "查询中稍等片刻"
    await session.send(prompt)
    Test_Recent_Sessions_report = await Test_data_source.Tset_Select_Recent_Sessions(Test_Quer_Recent_Sessions)
    await session.send(Test_Recent_Sessions_report, at_sender=True)

@Test_Recent_Sessions.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            session.state['Test_Quer_Recent_Sessions'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('要查询的ID不能为空，请重新输入')

    session.state[session.current_key] = stripped_arg


@on_command('Test_Vehicles', aliases=('测试载具', '测试查载具'),only_to_me=False)
async def Test_Vehicles(session: CommandSession):
    Test_Query_Vehicles = session.get('Test_Query_Vehicles', prompt='你想查询载具的ID是多少？')
    prompt = "查询中稍等片刻"
    await session.send(prompt)
    Test_Vehicles_report = await Test_data_source.Tset_Select_Vehicles(Test_Query_Vehicles)
    await session.send(Test_Vehicles_report, at_sender=True)


@Test_Vehicles.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            session.state['Test_Query_Vehicles'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('要查询的ID不能为空，请重新输入')

    session.state[session.current_key] = stripped_arg