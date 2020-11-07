from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from .Login_data_source import *



# 当用户输入关键字没有输入值时则提示
@on_command('Login', aliases=('注册','注册ID'), only_to_me=False)
async def Login(session: CommandSession):
    Query_Login = session.get('Query_Login', prompt='你想注册ID是多少？')
    Login_report = await get_Login(Query_Login)
    await session.send(Login_report, at_sender=True)


#  当用户输入关键字和值时直接运行
@Login.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['Query_Login'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('要注册的ID不能为空，请重新输入')

    session.state[session.current_key] = stripped_arg