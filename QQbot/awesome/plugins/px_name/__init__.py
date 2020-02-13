from nonebot import on_command, CommandSession
from .px_name_data_source import *


__plugin_name__ = '培训公司查询'
__plugin_usage__ = r"""
命令：培训名称/查培训名称/培训查询/查询培训/培训名字/是不是培训

培训名称 xxx公司
""".strip()


@on_command('px_name_select', aliases=('培训名称', '查培训名称', '培训查询', '查询培训', '培训名字', '是不是培训'), only_to_me=False)
async def px_name_select(session: CommandSession):
    companyName = session.get('query_px_name', prompt='你想查询是否培训公司的名称是什么？')
    result = await queryByName(companyName)
    print(result)
    await session.send(result)


@px_name_select.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            session.state['query_px_name'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('要查询的名称不能为空，请重新输入')

    session.state[session.current_key] = stripped_arg