import re
import requests
from lxml import etree
import time


async def dingxiang2(a):
    if a == '湖北':
        return area(0)
    elif a == '浙江':
        return area(1)
    elif a == '广东':
        return area(2)
    elif a == '湖南':
        return area(4)
    elif a == '河南':
        return area(3)
    elif a == '安徽':
        return area(5)
    elif a == '重庆':
        return area(7)
    elif a == '山东':
        return area(10)
    elif a == '江西':
        return area(6)
    elif a == '四川':
        return area(9)
    elif a == '江苏':
        return area(8)
    elif a == '北京':
        return area(11)
    elif a == '福建':
        return area(13)
    elif a == '上海':
        return area(12)
    elif a == '广西':
        return area(15)
    elif a == '陕西':
        return area(14)
    elif a == '河北':
        return area(17)
    elif a == '云南':
        return area(16)
    elif a == '海南':
        return area(20)
    elif a == '黑龙江':
        return area(18)
    elif a == '辽宁':
        return area(19)
    elif a == '山西':
        return area(21)
    elif a == '天津':
        return area(22)
    elif a == '甘肃':
        return area(23)
    elif a == '内蒙古':
        return area(26)
    elif a == '新疆':
        return area(28)
    elif a == '宁夏':
        return area(25)
    elif a == '贵州':
        return area(24)
    elif a == '吉林':
        return area(27)
    elif a == '青海':
        return area(30)
    elif a == '台湾':
        return area(31)
    elif a == '香港':
        return area(29)
    elif a == '澳门':
        return area(32)
    elif a == '西藏':
        return area(33)
    elif a == '全国':
        return dingxiang()
    else:
        comment = '全国新型肺炎疫情实时动态\n丁香医生版:\nhttps://3g.dxy.cn/newh5/view/pneumonia\n网易版:\nhttp://news.163.com/special/epidemic/\n腾讯版:\nhttps://news.qq.com//zt2020/page/feiyan.htm\n腾讯辟谣平台:\nhttps://vp.fact.qq.com/home'
        return comment


def area(a):
    import requests
    import time
    import json
    url = "https://3g.dxy.cn/newh5/view/pneumonia"
    headers = {
        "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    htmlContent = response.content.decode("utf-8")
    patt = 'window.getAreaStat = (.*?)}catch\(e\){}'
    s = re.findall(string=htmlContent, pattern=patt)
    c = json.loads(s[0])
    d = c[a]
    Start_Time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    time1 = "查询时间：" + Start_Time + '\n'
    # 省名
    provinceName = d['provinceName']
    # 省确诊
    confirmedCount = d['confirmedCount']
    # 省治愈
    curedCount = d['curedCount']
    # 省死亡
    deadCount = d['deadCount']
    comment1 = str(provinceName) + ' ' + '确诊:' + str(confirmedCount) + '例' + ',治愈:' + str(curedCount) + '例' + ',死亡:' + str(deadCount) + '例'
    f = d['cities']
    # 城市信息
    k = ''
    for a in f:
        l = ''
        cityName = a['cityName']
        confirmedCount = a['confirmedCount']
        curedCount = a['curedCount']
        deadCount = a['deadCount']
        l = k + str(cityName) + ' 确诊:' + str(confirmedCount) + '例' + ',治愈:' + str(curedCount) + '例' + ',死亡:' + str(
            deadCount) + '例' + '\n'
        k = l
    return time1 + comment1 + '\n下级城市:\n' + k + '\n数据来源:丁香医生'

def area1(a):
    import requests
    import time
    url = "http://api.maxlv.org:5012/api/info"
    headers = {
        "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }
    # proxies = {
    #     'http': 'username:password@125.123.122.178:9999',
    # }
    response = requests.get(url, headers=headers)
    print(response.text)
    c = response.json()
    Start_Time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    time1 = "查询时间：" + Start_Time + '\n'
    d = c['caseList'][a]
    # 省信息
    e = d['area']
    confirmed = d['confirmed']
    crued = d['crued']
    died = d['died']
    if crued == '' and died == '':
        crued = '0'
        died = '0'
        comment1 = e + ' ' + '确诊:' + str(confirmed) + '例' + ',治愈:' + str(crued) + '例' + ',死亡:' + str(died) + '例'
    elif crued == '':
        crued = '0'
        comment1 = e + ' ' + '确诊:' + str(confirmed) + '例' + ',治愈:' + str(crued) + '例' + ',死亡:' + str(died) + '例'
    elif died == '':
        died = '0'
        comment1 = e + ' ' + '确诊:' + str(confirmed) + '例' + ',治愈:' + str(crued) + '例' + ',死亡:' + str(died) + '例'
    comment1 = e + ' ' + '确诊:' + str(confirmed) + '例' + ',治愈:' + str(crued) + '例' + ',死亡:' + str(died) + '例'
    return time1 + comment1 + '\n数据来源:丁香医生'




def dingxiang():
    import json

    url = "https://3g.dxy.cn/newh5/view/pneumonia"
    headers = {
        "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }
    # proxies = {
    #     'http': 'username:password@125.123.122.178:9999',
    # }
    try:
        response = requests.get(url, headers=headers)
        htmlContent = response.content.decode("utf-8")
        # 2.将html解析成一个xpath对象
        xpath = etree.HTML(htmlContent)
        # 全国统计
        patt = '"countRemark":"",(.*?),"virus":"新型冠状病毒'
        s = re.findall(string=htmlContent, pattern=patt)
        f = "{%s}" % s[0]
        c = json.loads(f)
        d = c["confirmedCount"]
        e = c["suspectedCount"]
        # 治愈
        f = c["curedCount"]
        g = c["deadCount"]
        # 截止时间
        # patt = '<div class="title___2d1_B"><span>(.*?)</span><em><img alt="question"'
        # s1 = re.findall(string=htmlContent, pattern=patt)
        # print(s1)
        Start_Time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        time1 = "查询时间：" + Start_Time + '\n'
        s3 = time1 + '全国新型肺炎疫情实时动态：\n' +'全国确诊:'+str(d)+'例'+',疑似:'+str(e)+'例'+',治愈:'+str(f)+'例'+',死亡:'+str(g)+'例'+'\n'+ '疑似病例数来自国家卫健委数据，目前为全国数据'+'\n数据来源:丁香医生'
        return s3
    except:
        comment = '全国新型肺炎疫情实时动态\n丁香医生版:\nhttps://3g.dxy.cn/newh5/view/pneumonia\n网易版:\nhttp://news.163.com/special/epidemic/\n腾讯版:\nhttps://news.qq.com//zt2020/page/feiyan.htm\n腾讯辟谣平台:\nhttps://vp.fact.qq.com/home'
        return comment