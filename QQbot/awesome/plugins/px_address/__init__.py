from nonebot import on_command, CommandSession
from .px_address_data_source import *

__plugin_name__ = '培训地址查询'
__plugin_usage__ = r"""
命令：培训地址/查培训地址

培训地址 天府三街
""".strip()


@on_command('px_address_select', aliases=('培训地址', '查培训地址'), only_to_me=False)
async def px_address_select(session: CommandSession):
    address = session.get('query_px_address', prompt='你想查询是否培训公司的地址是什么？')
    # prompt = "查询中稍等片刻"
    # await session.send(prompt)
    px_address_select_report = await queryByAddress(address)
    await session.send(px_address_select_report)


@px_address_select.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            session.state['query_px_address'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('要查询的ID不能为空，请重新输入')

    session.state[session.current_key] = stripped_arg