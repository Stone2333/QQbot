import pymysql
import re

def Select_company_name(company_name):
    a = re.findall(r'[^\*"/:?\\|;\-\=]', company_name, re.S)
    company_name1 = "".join(a)
    if company_name1 == '':
        company_name1 = 'nmsl'
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="pxc")
    # cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor = db.cursor()
    sql = 'SELECT company_name,company_address FROM pxc_data_company WHERE company_name like "%{}%"'.format(company_name1)
    print(sql)
    cursor.execute(sql)
    db.commit()
    company_name_content = cursor.fetchall()
    # 将元组转换成列表
    company_name_content_list = list(company_name_content)
    company_name_list_join = []
    for index in range(len(company_name_content_list)):
        company_name_address = list(company_name_content[index])
        for company_name_address_list in range(len(company_name_address)):
            company_name_list_join.append(company_name_address[company_name_address_list])
    print(company_name_list_join)
    cursor.close()
    db.close()
    return company_name_list_join

def Select_company_address(company_address):
    a = re.findall(r'[^\*"/:?\\|;\-\=]', company_address, re.S)
    company_address1 = "".join(a)
    if company_address1 == '':
        company_address1 = 'nmsl'
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="pxc")
    cursor = db.cursor()
    sql = 'SELECT company_name,company_address FROM pxc_data_company WHERE company_address like "%{}%"'.format(company_address1)
    print(sql)
    cursor.execute(sql)
    db.commit()
    company_address_content = cursor.fetchall()
    # 将元组转换成列表
    company_address_content_list = list(company_address_content)
    company_address_list_join = []
    for index in range(len(company_address_content_list)):
        company_name_address = list(company_address_content[index])
        for company_name_address_list in range(len(company_name_address)):
            company_address_list_join.append(company_name_address[company_name_address_list])
    print(company_address_list_join)
    cursor.close()
    db.close()
    return company_address_list_join

    # return company_name_content_list



if __name__ == "__main__":
    Select_company_name('成都')
#     Select_company_address("天府三街新希望国际B座20楼2003室")

