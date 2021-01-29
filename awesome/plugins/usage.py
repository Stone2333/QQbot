# -*- coding=utf-8 -*-
import nonebot
from nonebot import on_command, CommandSession


@on_command('usage', aliases=['群列表', '群号'], only_to_me=False)
async def _(session: CommandSession):
    # 获取设置了名称的插件列表
    bot = nonebot.get_bot()
    list = await bot.get_group_list()
    print(list)
    str_list = str(list)
    await session.send(str_list)
    # plugins = list(filter(lambda p: p.name, nonebot.get_loaded_plugins()))
    # arg = session.current_arg_text.strip().lower()
    # if not arg:
    #     # 如果用户没有发送参数，则发送功能列表
    #     await session.send(
    #         '我现在支持的功能有：\n' + '\n'.join(p.name for p in plugins))
    #     return
    #
    # # 如果发了参数则发送相应命令的使用帮助
    # for p in plugins:
    #     if p.name.lower() == arg:
    #         await session.send(p.usage)

#


# c = [{'group_id': 248979909, 'group_name': '猎杀🍟「CPH」「WAM」「AC」', 'max_member_count': 500, 'member_count': 215},{'group_id': 533108821, 'group_name': 'gay酒小窝（鸽子窝）', 'max_member_count': 500, 'member_count': 276}, {'group_id': 615947920, 'group_name': '圆环之理炼战治凯厂涩图营业中', 'max_member_count': 500, 'member_count': 486}, {'group_id': 619439333, 'group_name': '战地翻车中队', 'max_member_count': 500, 'member_count': 444}, {'group_id': 620261056, 'group_name': '战地1/AC萌新交流群', 'max_member_count': 2000, 'member_count': 1614}, {'group_id': 631675855, 'group_name': 'ARXI 大🐦转转转酒吧', 'max_member_count': 2000, 'member_count': 245}, {'group_id': 694769671, 'group_name': '🇨🇳反坦克联盟小组🇨🇳', 'max_member_count': 1000, 'member_count': 238}, {'group_id': 711318224, 'group_name': '战地1私服花坛观光旅游考察团', 'max_member_count': 500, 'member_count': 447}, {'group_id': 729032552, 'group_name': '战地1/bf1/BF1服务器ZBW', 'max_member_count': 1000, 'member_count': 725}, {'group_id': 730461957, 'group_name': '战地一Anti Hololive战队闲聊开黑群', 'max_member_count': 500, 'member_count': 120}, {'group_id': 806512517, 'group_name': '[HJ服务器]战地一烬燃这么好玩？', 'max_member_count': 1000, 'member_count': 510}, {'group_id': 813818294, 'group_name': 'Ana.甲亢康复训练中心', 'max_member_count': 200, 'member_count': 69}, {'group_id': 814333761, 'group_name': 'AA交流群', 'max_member_count': 500, 'member_count': 177}, {'group_id': 817398968, 'group_name': '战地1/战地5 Hotel Squad', 'max_member_count': 2000, 'member_count': 1067}, {'group_id': 824904534, 'group_name': 'Kano \\守护最好二次元/', 'max_member_count': 500, 'member_count': 80}, {'group_id': 832748692, 'group_name': 'INN乐了细说服务器', 'max_member_count': 1000, 'member_count': 582}, {'group_id': 854627009, 'group_name': 'chop迫击炮发射阵地', 'max_member_count': 200, 'member_count': 199}, {'group_id': 864770374, 'group_name': '[bf1]rabbit house', 'max_member_count': 500, 'member_count': 86}, {'group_id': 930873837, 'group_name': 'INKA服务器交流群', 'max_member_count':200, 'member_count': 176}, {'group_id': 972669354, 'group_name': 'APX战地1/一及其他游戏交流群', 'max_member_count': 500, 'member_count': 454}, {'group_id': 980772107, 'group_name': '战地一MSZ权限服反馈群', 'max_member_count': 500, 'member_count': 181}, {'group_id': 1022853709, 'group_name': 'BF1豌豆私服', 'max_member_count': 500, 'member_count': 158}, {'group_id': 1025316951, 'group_name': '259LUXU战地联动群', 'max_member_count': 500, 'member_count': 196}, {'group_id': 1027381497, 'group_name': '【NFZ】服务器，暖服，踢挂，交友🙋\u200d♂️', 'max_member_count': 2000, 'member_count': 428}, {'group_id': 1030431427, 'group_name': '战地一/miru私服2⃣️群🥶 ', 'max_member_count': 2000, 'member_count': 531}, {'group_id': 1033551767, 'group_name': '小阿桔医学院', 'max_member_count': 500, 'member_count': 383}, {'group_id': 1060185168, 'group_name': 'CNNB战地xp交流群', 'max_member_count': 2000, 'member_count': 1323}, {'group_id': 1104387658, 'group_name': 'Nah🈲迫击炮150白名单蕉♂流中心', 'max_member_count': 1000, 'member_count': 484}, {'group_id': 1106491550, 'group_name': '【SHH】战地薯条开黑群', 'max_member_count': 500, 'member_count': 131}, {'group_id': 1121027414, 'group_name': '战地1【GHYNB】大鸟转转转酒吧', 'max_member_count': 2000, 'member_count': 326}, {'group_id': 1126266560, 'group_name': '战地1 luhua 服务器', 'max_member_count': 500, 'member_count': 299}, {'group_id': 1130295068, 'group_name': '战地1/BF1服务器【1S】', 'max_member_count': 500, 'member_count': 457}, {'group_id': 1134253847, 'group_name': '新东方厨力交流群', 'max_member_count': 500, 'member_count': 68}, {'group_id': 1140891157, 'group_name': '♂AKAME粉丝群 ghs服务器♂', 'max_member_count': 500, 'member_count': 468}, {'group_id': 1153476318, 'group_name': 'FF GAMING内部服务器', 'max_member_count': 500, 'member_count': 75}, {'group_id': 1163816643, 'group_name': 'PF萌新服务器', 'max_member_count': 200, 'member_count': 139}]
# d = {}
# for i in c:
#     group_name = i['group_name']
#     group_id = i['group_id']
#     d[group_id] = group_name
# print(d)