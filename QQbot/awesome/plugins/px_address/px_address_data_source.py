# *-* coding:utf8 *-*

from QQbot.orm.sessionUtil import *


async def queryByAddress(address: str):
    px = mySession.query(TrainCompany).filter(
        TrainCompany.company_address.like("%" + address + "%")
    ).all()

    print(px)
    if not px:
        null = "该地址未在培训库中存在"
        print("该地址未在培训库中存在")
        return null

    else:
        f = ""
        for index, item in enumerate(px):
            f += '培训不得house\n{}:培训公司名称:{}\n地址:{}\n'.format(index + 1, item.company_name, item.company_address)
        print(f)
        return f
