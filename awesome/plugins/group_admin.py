from nonebot import on_request, RequestSession
from nonebot import on_notice, NoticeSession
import nonebot
import re

# 将函数注册为群请求处理器
@on_request('group')
async def _(session: RequestSession):
    # 判断验证信息是否符合要求  
    c = session.event.comment
    print(c)
    pattern = '答案：(.*)'
    name = re.findall(pattern, c)
    if name[0] in ['贴吧','百度贴吧','服务器','游戏里','B站','b站','伺服器','ZBW','zbw','小破站','破站','B','朋友介绍','熟人介绍','朋友推荐','私服','有挂','服务器有挂']:
	
        # 验证信息正确，同意入群
        await session.approve()
        return
    pass
    
    # 验证信息错误，拒绝入群
    # await session.reject('请说暗号')


# 将函数注册为群成员增加通知处理器
@on_notice('group_increase')
async def _(session: NoticeSession):
    if session.event.group_id == 729032552:
        # 发送欢迎消息
        await session.send('欢迎新朋友～,请将群名称改为橘子id')



