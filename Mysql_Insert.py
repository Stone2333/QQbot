﻿import pymysql



# 插入服务器名称和服务器ID
def Insert_Server_Id(servername, serverid):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = '''
          INSERT INTO `server_id` (servername, serverid) 
          VALUES ("{}","{}")
          '''.format(servername, serverid)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    print(servername, "服务器ID数据库插入成功")


# 插入游戏名称
def Insert_User(name):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = '''
          INSERT INTO `user` (username) 
          VALUES ("{}") 
          '''.format(name)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    print(name, "游戏ID数据库插入成功")


# 插入战绩信息
def Insert_Overview(name, score_min, kd_ratio, win_percent, kills_game, kills_min, infantry_kpm, infantry_kd, vehicle_kills, vehicle_kpm, skill, accuracy):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = '''
          INSERT INTO `overview` (name, score_min, kd_ratio, win_percent, kills_game, kills_min, infantry_kpm, infantry_kd, vehicle_kills, vehicle_kpm, skill, accuracy) 
          VALUES ("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}") 
          '''.format(name, score_min, kd_ratio, win_percent, kills_game, kills_min, infantry_kpm, infantry_kd, vehicle_kills, vehicle_kpm, skill, accuracy)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    print(name, "战绩数据库插入成功")


# 插入载具信息
def Insert_Vehicles(name, vehiclesname, kills, kpm, destroyed, vehiclesname1, kills1, kpm1, destroyed1, vehiclesname2, kills2, kpm2, destroyed2):
    db = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="123456",
        db="bf1")
    cursor = db.cursor()
    sql = '''
          INSERT INTO `vehicles` (name, VehiclesName, KILLS, KPM, Destroyed, VehiclesName1, KILLS1, KPM1, Destroyed1, VehiclesName2, KILLS2, KPM2, Destroyed2)
          VALUES ("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")
          '''.format(name, vehiclesname, kills, kpm, destroyed, vehiclesname1, kills1, kpm1, destroyed1, vehiclesname2, kills2, kpm2, destroyed2)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
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
    sql = '''
          INSERT INTO `recent_sessions` (name, spm, kd, kpm, game_play_time, game_time)
          VALUES ("{}","{}","{}","{}","{}","{}")
          '''.format(name, spm, kd, kpm, game_play_time, game_time)
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
          '''.format(groupid, module, module, number)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    print('数量插入成功')
