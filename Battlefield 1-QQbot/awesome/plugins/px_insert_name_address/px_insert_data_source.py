import px_insert
import re

async def get_px_insert(px_insert_insert):
    px_insert_str = px_insert_insert
    pattern = '(.*),'
    name = re.findall(pattern, px_insert_str)
    insert_name = name[0]
    pattern1 = ',(.*)'
    address = re.findall(pattern1, px_insert_str)
    insert_address = address[0]
    px_insert.px_insert(insert_name, insert_address)
    prompt = '培训公司信息入库成功'
    return prompt