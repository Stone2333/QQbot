# *-* coding:utf8 *-*
import datetime
import re
import requests
import time
import json
import math


async def dingxiang(address):
    try:
        if address == '全国':
            return queryAll()
        else:
            return queryByAddress(address)
    except:
        comment = '全国新型肺炎疫情实时动态\n丁香医生版:\nhttps://3g.dxy.cn/newh5/view/pneumonia\n网易版:\nhttp://news.163.com/special/epidemic/\n腾讯版:\nhttps://news.qq.com//zt2020/page/feiyan.htm\n腾讯辟谣平台:\nhttps://vp.fact.qq.com/home'
        return comment


# 获取网页数据
def getData() -> str:
    headers = {
        "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }
    res = requests.get("https://3g.dxy.cn/newh5/view/pneumonia", headers=headers)
    content = res.content.decode(encoding="utf-8", errors="error")
    return content


# 根据地方查询
def queryByAddress(address: str):
    content = getData()
    pattern = re.compile(r'window.getAreaStat = (.*?)}catch\(e\){}')
    result = pattern.findall(content)

    # 全部省市key,value
    allData = {}
    datas = json.loads(result[0])
    for item in datas:
        allData[item["provinceName"]] = {
            "name" : item["provinceName"],                                  #名称
            "provinceName": item["provinceName"],
            "confirmedCount": item["confirmedCount"],                       #累计确诊
            "currentConfirmedCount" : item["currentConfirmedCount"],        #当前确诊
            "deadCount": item["deadCount"],                                 #死亡数
            "curedCount": item["curedCount"],                               #治愈数
            "locationId": item["locationId"],                               #地方id
        }
        allData[item["provinceShortName"]] = {
            "name": item["provinceShortName"],
            "provinceShortName": item["provinceShortName"],
            "confirmedCount": item["confirmedCount"],
            "currentConfirmedCount": item["currentConfirmedCount"],
            "deadCount": item["deadCount"],
            "curedCount": item["curedCount"],
            "locationId": item["locationId"],
        }
        for city in item['cities']:
            allData[city["cityName"]] = {
                "name": city["cityName"],
                "cityName": city["cityName"],
                "confirmedCount": city["confirmedCount"],
                "currentConfirmedCount": city["currentConfirmedCount"],
                "deadCount": city["deadCount"],
                "curedCount": city["curedCount"],
                "locationId": city["locationId"],
            }
    queryTime = "查询时间: {}\n".format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    item = allData[address]
    # 省份数据
    province_locationId = math.floor(item["locationId"] / 10000) * 10000
    province = list(filter(lambda temp: temp["locationId"] == province_locationId and "provinceName" in temp.keys(),allData.values()))[0]
    provinceStr = "{} 现存确诊: {}例,累计确诊: {}例,治愈:{}例,死亡{}例\n".format(province["name"], province["currentConfirmedCount"],province["confirmedCount"], province["curedCount"],province["deadCount"])

    # 城市数据,判断如果是查询的城市,那么还需要拼接城市的信息
    cityStr = ""
    if item["locationId"] % 10000 != 0:
        cityStr = "{} 现存确诊: {}例,累计确诊: {}例,治愈:{}例,死亡{}例\n".format(item["name"], item["currentConfirmedCount"],item["confirmedCount"], item["curedCount"],item["deadCount"])

    endStr = "数据来源:丁香医生"
    return '{}{}{}{}'.format(queryTime,provinceStr,cityStr,endStr)

# 查询全国数据
def queryAll():
    content = getData()
    pattern = re.compile(r'window.getStatisticsService = (.*?)}catch\(e\){}')
    result = pattern.findall(content)
    data = json.loads(result[0])
    queryTime = "查询时间: {}\n".format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    updateTime = "更新时间: {}\n".format(datetime.datetime.fromtimestamp(data["modifyTime"] / 1000).strftime('%Y-%m-%d %H:%M:%S', ))
    startStr = '全国新型肺炎疫情实时动态：\n'
    data0Str = '累计确诊:{}例,今日新增{}例\n'.format(data["confirmedCount"],data["confirmedIncr"])
    data1Str = '现存确诊:{}例,今日新增{}例\n'.format(data["currentConfirmedCount"],data["currentConfirmedIncr"])
    data2Str = '现存疑似:{}例,今日新增{}例\n'.format(data["suspectedCount"],data["suspectedIncr"])
    data3Str = '累计治愈:{}例,今日新增{}例\n'.format(data["curedCount"],data["curedIncr"])
    data4Str = '累计重症:{}例,今日新增{}例\n'.format(data["seriousCount"],data["seriousIncr"])
    data5Str = '累计死亡:{}例,今日新增{}例\n'.format(data["deadCount"],data["deadIncr"])
    endStr = "疑似病例数来自国家卫健委数据，目前为全国数据\n数据来源:丁香医生"
    return '{}{}{}{}{}{}{}{}{}{}'.format(queryTime,updateTime,startStr,data0Str,data1Str,data2Str,data3Str,data4Str,data5Str,endStr)

if __name__ == '__main__':
    # print(queryByAddress('北京'))
    # print(queryByAddress('朝阳区'))
    # print(queryByAddress('四川'))
    # print(queryByAddress('成都'))
    # print('=='*100)
    # print(queryByAddress('广安'))

    print(queryAll())

    # print('=='*100)