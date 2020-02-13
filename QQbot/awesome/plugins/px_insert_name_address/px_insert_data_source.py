# *-* coding:utf8 *-*

import re
from QQbot.orm.sessionUtil import *


async def save(data: str):
    px_insert_str = data
    pattern = '(.*),'
    name = re.findall(pattern, px_insert_str)
    insert_name = name[0]
    pattern1 = ',(.*)'
    address = re.findall(pattern1, px_insert_str)
    insert_address = address[0]
    mySession.add(TrainCompany(company_name=insert_name, company_address=insert_address, create_time=now()))
    mySession.commit()
    prompt = '培训公司信息入库成功'
    return prompt
