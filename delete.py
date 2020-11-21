import pymysql



def delete_recent_sessions(name):
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