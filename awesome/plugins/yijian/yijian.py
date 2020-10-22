import nonebot
from aiocqhttp.exceptions import Error as CQHttpError
import Mysql_Insert

async def yijian2(message, qq):
    Mysql_Insert.Insert_idea(qq, message)
    return '意见添加成功'