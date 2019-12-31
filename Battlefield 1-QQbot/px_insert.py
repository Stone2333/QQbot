import pymysql
import re



# 插入培训公司信息
def px_insert(company_name, company_address):
    a = re.findall(r'[^\*"/:?\\|;\-\=]', company_name, re.S)
    company_name1 = "".join(a)
    company_address1 = "".join(a)
    if company_name1 == '' and company_address1 == '':
        p = '培训地址和名字不能为空'
        return p
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="pxc")
    cursor = db.cursor()
    sql = '''
          INSERT INTO `pxc_data_company` (company_name,company_address) 
          VALUES ("{}","{}") 
          '''.format(company_name, company_address)
    cursor.execute(sql)
    db.commit()
    p = '培训公司信息数据库入库成功'
    return p 