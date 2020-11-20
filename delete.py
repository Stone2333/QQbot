import DB

db = DB.MysqlDB('127.0.0.1', 'root', '123456', 'bf1')


def delete_recent_sessions(name):
    sql = """
    DELETE
    FROM `recent_sessions`
    WHERE name = "{}"
    
    """.format(name)
    db.execute(sql)
    db.close()