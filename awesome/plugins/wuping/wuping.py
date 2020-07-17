import Mysql_Insert
import Mysql_Update
import requests
import pymysql
import xmltodict
import json

async def get_wuping(name: str) -> str:
    try:
        if name == '矿价':
            url = "https://www.ceve-market.org/api/evemon"
            headers = {
                "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
            }
            response = requests.get(url, headers=headers)
            string = response.text
            dic = xmltodict.parse(string, encoding='utf-8')
            json_string = json.dumps(dic, indent=4, ensure_ascii=False)
            json_join = json.loads(json_string)
            minerals = json_join['minerals']['mineral']
            k = ''
            for i in minerals:
                l = ''
                name = i['name']
                price = i['price']
                l = k + '{}\n价格:{}\n'.format(name, price)
                k = l
            return '吉他矿价:\n' + k + '数据来源:ceve-market'
        else:
            d = select('select typeid from eve where name = "{}"'.format(name))
            if d == ():
                c = select('select * from eve where name LIKE "%{}%" LIMIT 5'.format(name))
                if c == ():
                    return '输入的物品名称不正确/不存在，请重新输入'
                else:
                    k = ''
                    for i in c:
                        l = ''
                        url = "https://www.ceve-market.org/api/market/region/10000002/type/{}.json".format(i[0])
                        headers = {
                            "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
                        }
                        response = requests.get(url, headers=headers)
                        string = response.json()
                        buydict = string['buy']
                        buymax = buydict['max']
                        buymin = buydict['min']
                        max = format(buymax, ',')
                        min = format(buymin, ',')
                        string2 = '收价订单:\n最高:{}\n最低:{}'.format(max, min)
                        selldict = string['sell']
                        sellmax = selldict['max']
                        sellmin = selldict['min']
                        max = format(sellmax, ',')
                        min = format(sellmin, ',')
                        string1 = '卖价订单:\n最高:{}\n最低:{}\n'.format(max, min)
                        string = i[1] + '\n' + string1 + string2
                        l = k + '\n'+ string
                        k = l
                    return '吉他物价:'+ k + '\n' + '数据来源:ceve-market'
            else:
                c = select('select typeid from eve where name = "{}"'.format(name))
                id = c[0][0]
                url = "https://www.ceve-market.org/api/market/region/10000002/type/{}.json".format(id)
                headers = {
                    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
                }
                response = requests.get(url, headers=headers)
                string = response.json()
                buydict = string['buy']
                buymax = buydict['max']
                buymin = buydict['min']
                max = format(buymax, ',')
                min = format(buymin, ',')
                string2 = '收价订单:\n最高:{}\n最低:{}'.format(max, min)
                selldict = string['sell']
                sellmax = selldict['max']
                sellmin = selldict['min']
                max = format(sellmax, ',')
                min = format(sellmin, ',')
                string1 = '卖价订单:\n最高:{}\n最低:{}\n'.format(max, min)
                string = name + '\n' + string1 + string2 + '\n' + '数据来源:ceve-market'
                return string
    except:
        string = "EVE市场接口尚未恢复,恢复之后即可正常查询使用"
        return string
    
def select(sql):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    # cursor = db.cursor(pymysql.cursors.DictCursor)
    sql = '''{}'''.format(sql)
    cursor.execute(sql)
    db.commit()
    content = cursor.fetchall()
    cursor.close()
    db.close()
    return content


if __name__ == '__main__':
    get_wuping('狂怒')