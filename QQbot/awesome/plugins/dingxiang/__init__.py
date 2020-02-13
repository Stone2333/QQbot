from nonebot import on_command, CommandSession
from .dingxiang_datasource import *


__plugin_name__ = '疫情查询'
__plugin_usage__ = r"""
疫情查询

疫情 全国
疫情 成都
""".strip()

# 当用户输入关键字没有输入值时则提示
@on_command('query', aliases=('疫情查询','疫情'), only_to_me=False)
async def cha1(session: CommandSession):
    address = session.get('query_pneumonia_address', prompt='请输入"全国"')
    chaxun = await dingxiang(address)
    await session.send(chaxun)


#  当用户输入关键字和值时直接运行
@cha1.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['query_pneumonia_address'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('请输入"全国"，请重新输入')

    session.state[session.current_key] = stripped_arg
