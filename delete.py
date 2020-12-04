import pymysql



def delete_recent_sessions(name):
    """删除最近战绩"""
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = """
    DELETE
    FROM `recent_sessions`
    WHERE name = "{}"
    
    """.format(name)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()


def delete_vehicles(name):
    """删除载具数据"""
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = """
    DELETE
    FROM `new_vehicles`
    WHERE name = "{}"

    """.format(name)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()


def delete_weapons(name):
    """删除武器信息"""
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = """
    DELETE
    FROM `new_weapons`
    WHERE name = "{}"
    """.format(name)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()