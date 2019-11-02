import requests
from lxml import etree
import re

async def get_Overview(Query_Overview: str) -> str:
    url = "https://battlefieldtracker.com/bf1/search?platform=pc&name="
    url_join = url + Query_Overview
    headers = {
        "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }
    # proxies = {
    #     'http': 'username:password@125.123.122.178:9999',
    # }
    response = requests.get(url_join, headers=headers)
    html = response.content.decode("utf-8")
    # 过滤html
    pattern = '"Field":.*?,"Value":(.*?)\},\{'
    string = re.findall(pattern, html, re.S)
    # 正则过滤后string转换成列表
    res = list(string)
    try:
        # BTRSCORE = "BTR分数:" + res[0]
        # BTR_MIN = "BTR/分钟:" + res[1]
        SCORE_MIN = "分数/分钟:" + res[2]
        KD_RATIO = "K/D比:" + res[3]
        WIN_PERCENT = "胜率:" + res[4]
        KILLS_GAME = "场均击杀:" + res[5]
        KILLS_MIN = "杀敌/分钟:" + res[6]
        INFANTRY_KPM = "步兵KPM:" + res[7]
        INFANTRY_KD = "步兵KD:" + res[8]
        VEHICLE_KILLS = "载具击杀:" + res[9]
        VEHICLE_KPM = "载具KPM:" + res[10]
        SKILL = "技巧值:" + res[11]
        ACCURACY = "准度:" + res[15]
        # 存进列表
        Overview_list = ["\n游戏ID:" + Query_Overview, SCORE_MIN, KD_RATIO, WIN_PERCENT, KILLS_GAME, KILLS_MIN, INFANTRY_KPM, INFANTRY_KD,
                VEHICLE_KILLS, VEHICLE_KPM, SKILL, ACCURACY]
        # 去逗号
        Overview_str = (' \n'.join(Overview_list))
        return Overview_str
    except:
        error = 'ID错误或网络问题，请稍后重试'
        return error