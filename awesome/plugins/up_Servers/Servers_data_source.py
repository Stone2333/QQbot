import requests
from lxml import etree
import re
import Mysql_Insert
import Mysql_Update
import Mysql_Select


async def get_Servers(Quer_Servers: str) -> str:
    Servers = Quer_Servers
    pattern = '(.*),'
    name = re.findall(pattern, Servers)
    update_name = name[0]
    pattern1 = ',(.*)'
    id = re.findall(pattern1, Servers)
    update_id = id[0]
    name = Mysql_Select.Select_Server_Id(update_name)
    if name == []:
        null = "服务器不存在"
        return null
    else:
        Mysql_Update.Update_Server_Id(update_name, update_id)
        prompt = update_name + '服务器信息更新成功'
        return prompt

