import pymysql
import DB


def db():
    """
    数据库对象

    :return: 数据库对象
    """
    d = DB.MysqlDB(
        host='127.0.0.1',
        user='root',
        password='123456',
        db='bf1')
    return d

# 插入服务器名称和服务器ID
def insert_server_id(server_name, server_id):
    """
    插入服务器名称和服务器id

    :param server_name: 服务器简称
    :param server_id: 服务器唯一码
    :return:
    """
    sql = '''
          INSERT INTO `server_id` (servername, serverid) 
          VALUES ("{}","{}")
          '''.format(server_name, server_id)
    db().execute(sql)
    db().close()
    print(server_name, "服务器ID数据库插入成功")


# 插入游戏名称
def insert_user(name):
    """
    插入user表游戏名称

    :param name: 游戏id
    :return:
    """
    sql = '''
          INSERT INTO `user` (username) 
          VALUES ("{}") 
          '''.format(name)
    db().execute(sql)
    db().close()
    print(name, "游戏ID数据库插入成功")


# 插入战绩信息
def insert_overview(name, score_min, kd_ratio, win_percent, kills_game, kills_min, infantry_kpm, infantry_kd, vehicle_kills, vehicle_kpm, skill, accuracy):
    """
    插入战绩信息

    :param name: 游戏id
    :param score_min: 每分钟得分数
    :param kd_ratio: kd比
    :param win_percent: 胜率
    :param kills_game: 游戏时间
    :param kills_min: 每分钟杀敌数
    :param infantry_kpm: 步兵每分钟杀敌数
    :param infantry_kd: 步兵kd
    :param vehicle_kills: 载具kd
    :param vehicle_kpm: 载具kpm
    :param skill: 技巧值
    :param accuracy: 准度
    :return:
    """
    sql = '''
          INSERT INTO `overview` (name, score_min, kd_ratio, win_percent, kills_game, kills_min, infantry_kpm, infantry_kd, vehicle_kills, vehicle_kpm, skill, accuracy) 
          VALUES ("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}") 
          '''.format(name, score_min, kd_ratio, win_percent, kills_game, kills_min, infantry_kpm, infantry_kd, vehicle_kills, vehicle_kpm, skill, accuracy)
    db().execute(sql)
    db().close()
    print(name, "战绩数据库插入成功")


# 插入载具信息
def insert_vehicles(name, vehiclesname, kills, kpm, destroyed, vehiclesname1, kills1, kpm1, destroyed1, vehiclesname2, kills2, kpm2, destroyed2):
    sql = '''
          INSERT INTO `vehicles` (name, VehiclesName, KILLS, KPM, Destroyed, VehiclesName1, KILLS1, KPM1, Destroyed1, VehiclesName2, KILLS2, KPM2, Destroyed2)
          VALUES ("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")
          '''.format(name, vehiclesname, kills, kpm, destroyed, vehiclesname1, kills1, kpm1, destroyed1, vehiclesname2, kills2, kpm2, destroyed2)
    db().execute(sql)
    db().close()
    print(name, "载具数据库插入成功")


# 插入武器信息
def Insert_Weapons(name, weaponsname, kills, kpm, accuracy, headshots, weaponsname1, kills1, kpm1, accuracy1, headshots1, weaponsname2, kills2, kpm2, accuracy2, headshots2):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = '''
          INSERT INTO `weapons` (name, weaponsname, kills, kpm, accuracy, headshots, weaponsname1, kills1, kpm1, accuracy1, headshots1, weaponsname2, kills2, kpm2, accuracy2, headshots2)
          VALUES ("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")
          '''.format(name, weaponsname, kills, kpm, accuracy, headshots, weaponsname1, kills1, kpm1, accuracy1, headshots1, weaponsname2, kills2, kpm2, accuracy2, headshots2)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    print(name, "武器数据库插入成功")


# 插入最近战绩
def Insert_Recent_Sessions(name, spm, kd, kpm, timeplayed, spm1, kd1, kpm1, timeplayed1, spm2, kd2, kpm2, timeplayed2):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = '''
          INSERT INTO `recent_sessions` (name, spm, kd, kpm, timeplayed, spm1, kd1, kpm1, timeplayed1, spm2, kd2, kpm2, timeplayed2) 
          VALUES ("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")
          '''.format(name, spm, kd, kpm, timeplayed, spm1, kd1, kpm1, timeplayed1, spm2, kd2, kpm2, timeplayed2)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    print(name, "最近战绩数据库插入成功")


# 插入服务器详细信息
def Insert_Servers(servername, name, maplist, prayers):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = '''
          INSERT INTO `server` (servername, name, maplist, prayers)
          VALUES ("{}","{}","{}","{}")
          '''.format(servername, name, maplist, prayers)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    print(servername, "服务器信息数据库插入成功")


# 插入意见
def Insert_idea(qq, idea):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = '''
          INSERT INTO `proposal` (qq,idea)
          VALUES ("{}","{}")
          '''.format(qq, idea)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    print(qq, "意见信息数据库插入成功")


def Insert_relevance(qq, username):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = '''
          INSERT INTO `relevance` (qq, username)
          VALUES ("{}","{}")
          '''.format(qq, username)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    print('游戏ID与QQ绑定成功')



def insert_recent_sessions(name, spm, kd, kpm, game_play_time, game_time):
    """
    插入最近信息

    :param name:
    :param spm:
    :param kd:
    :param kpm:
    :param game_play_time:
    :param game_time:
    :return:
    """
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = f'''
          INSERT INTO `recent_sessions` (name, spm, kd, kpm, game_play_time, game_time)
          VALUES ("{name}","{spm}","{kd}","{kpm}","{game_play_time}","{game_time}")
          '''
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    print(name, "最近战绩数据库插入成功")


def insert_statistics_number(groupid, module, number=1):
    """插入调用模块数量"""
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = '''
          INSERT INTO `statistics` (groupid, module, number)
          VALUES ("{}","{}","{}")
          '''.format(groupid, module, number)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    print('数量插入成功')


def insert_server(server_id, server_name, maplist, mode, prayers):
    """插入服务器信息"""
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = '''
          INSERT INTO `server` (server_id, server_name , maplist, mode, prayers)
          VALUES ("{}","{}","{}","{}","{}")
          '''.format(server_id, server_name, maplist, mode, prayers)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
