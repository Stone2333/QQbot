import pymysql


def px_insert(company_name,company_address):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="pxc")
    cursor = db.cursor()
    sql = 'INSERT INTO `pxc_data_company` (company_name,company_address) VALUES ("{}","{}") '.format(company_name,company_address)
    print(sql)
    cursor.execute(sql)
    db.commit()
    p = '培训公司信息数据库入库成功'
    return p 