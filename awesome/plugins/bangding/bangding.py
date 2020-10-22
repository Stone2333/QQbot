import nonebot
from aiocqhttp.exceptions import Error as CQHttpError
import Mysql_Insert
import Mysql_Select
import Mysql_Update

async def bangding2(message, qq):
    relevance = Mysql_Select.Select_Id(qq)
    if relevance == ():
        Mysql_Insert.Insert_relevance(qq, message)
        return '绑定ID成功'
    else:
        Mysql_Update.Update_ID(qq, message)
        return 'qq绑定id变更为:{}'.format(message)