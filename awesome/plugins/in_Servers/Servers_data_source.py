import requests
from lxml import etree
import re
import Mysql_Insert


async def get_Servers(Quer_Servers: str) -> str:
    Servers = Quer_Servers
    pattern = '(.*),'
    name = re.findall(pattern, Servers)
    insert_name = name[0]
    pattern1 = ',(.*)'
    address = re.findall(pattern1, Servers)
    insert_id = address[0]
    try:
        Mysql_Insert.insert_server_id(insert_name, insert_id)
        prompt = insert_name + '服务器信息入库成功'
        return prompt
    except:
        prompt = insert_name + '服务器信息已存在'
        return prompt


