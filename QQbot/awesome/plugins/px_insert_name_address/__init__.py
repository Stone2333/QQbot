from nonebot import on_command, CommandSession
from .px_insert_data_source import *

__plugin_name__ = '培训插入'
__plugin_usage__ = r"""
命令：插入培训/培训插入

培训插入 xxx培训公司,天府三街
""".strip()



@on_command('px_name_insert', aliases=('插入培训', '培训插入'), only_to_me=False)
async def px_name_insert(session: CommandSession):
    data = session.get('insert_px_data', prompt='你想插入的培训公司名称地址是什么？用英文逗号分隔')
    px_name_select_report = await save(data)
    await session.send(px_name_select_report)


@px_name_insert.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            session.state['insert_px_data'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('要查询的ID不能为空，请重新输入')

    session.state[session.current_key] = stripped_arg