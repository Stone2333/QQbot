import pymysql
import re



# 根据传入名称模糊查询
def Select_company_name(company_name):
    a = re.findall(r'[^\*"/:?\\|;\-\=]', company_name, re.S)
    company_name1 = "".join(a)
    if company_name1 == '':
        p = '培训名字不能为空'
        return p
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="pxc")
    # cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor = db.cursor()
    sql = '''
          SELECT company_name,company_address 
          FROM pxc_data_company 
          WHERE company_name 
          LIKE "%{}%"
          '''.format(company_name1)
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
    cursor.close()
    db.close()
    return company_name_list_join

# 根据传入地址模糊查询
def Select_company_address(company_address):
    a = re.findall(r'[^\*"/:?\\|;\-\=]', company_address, re.S)
    company_address1 = "".join(a)
    if company_address1 == '':
        p = '培训地址不能为空'
        return p
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="pxc")
    cursor = db.cursor()
    sql = '''
          SELECT company_name,company_address 
          FROM pxc_data_company 
          WHERE company_address 
          LIKE "%{}%"
          '''.format(company_address1)
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
    cursor.close()
    db.close()
    return company_address_list_join



if __name__ == "__main__":
    Select_company_name('成都')
#     Select_company_address("天府三街新希望国际B座20楼2003室")

