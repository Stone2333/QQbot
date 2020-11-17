import pymysql


class MysqlDB(object):
    """mysql 数据库"""

    def __init__(self, host, user, password, db):
        self.db = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db)
        self.cursor = self.db.cursor()

    def select(self, sql):
        self.cursor.execute(sql)
        self.db.commit()
        results = self.cursor.fetchall()
        return results

    def execute(self, sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except BaseException:
            self.db.rollback()

    def close(self):
        self.cursor.close()
        self.db.close()

