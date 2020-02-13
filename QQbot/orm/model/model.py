# coding: utf-8
from sqlalchemy import Column, String, TIMESTAMP
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Overview(Base):
    __tablename__ = 'overview'

    id = Column(INTEGER(20), primary_key=True, comment='自增ID')
    name = Column(String(255, 'utf8mb4_general_ci'), nullable=False, comment='游戏ID')
    score_min = Column(String(255, 'utf8mb4_general_ci'), comment='每分钟得分数')
    kd_ratio = Column(String(255, 'utf8mb4_general_ci'), comment='击杀/死亡比')
    win_percent = Column(String(255, 'utf8mb4_general_ci'), comment='胜率')
    kills_game = Column(String(255, 'utf8mb4_general_ci'), comment='场均击杀')
    kills_min = Column(String(255, 'utf8mb4_general_ci'), comment='每分钟击杀数')
    infantry_kpm = Column(String(255, 'utf8mb4_general_ci'), comment='步兵每分钟击杀数')
    infantry_kd = Column(String(255, 'utf8mb4_general_ci'), comment='步兵击杀/死亡比')
    vehicle_kills = Column(String(255, 'utf8mb4_general_ci'), comment='载具击杀数')
    vehicle_kpm = Column(String(255, 'utf8mb4_general_ci'), comment='载具每分钟击杀数')
    skill = Column(String(255, 'utf8mb4_general_ci'), comment='技巧值')
    accuracy = Column(String(255, 'utf8mb4_general_ci'), comment='准度')
    create_time = Column(TIMESTAMP)
    update_time = Column(TIMESTAMP)


class RecentSesion(Base):
    __tablename__ = 'recent_sesions'

    id = Column(INTEGER(20), primary_key=True, comment='自增ID')
    name = Column(String(255, 'utf8mb4_general_ci'), nullable=False, comment='游戏ID')
    spm = Column(String(255, 'utf8mb4_general_ci'), comment='每分钟得分数')
    kd = Column(String(255, 'utf8mb4_general_ci'), comment='击杀/死亡比')
    kpm = Column(String(255, 'utf8mb4_general_ci'), comment='每分钟击杀数 ')
    timeplayed = Column(String(255, 'utf8mb4_general_ci'), comment='游戏时间')
    create_time = Column(TIMESTAMP)
    update_time = Column(TIMESTAMP)


class Server(Base):
    __tablename__ = 'server'

    id = Column(INTEGER(20), primary_key=True, comment='自增ID')
    server_id = Column(INTEGER(15), nullable=False, comment='服务器ID')
    server_name = Column(String(255, 'utf8mb4_general_ci'), comment='服务器名称')
    maplist = Column(String(255, 'utf8mb4_general_ci'), comment='地图')
    prayers = Column(String(255, 'utf8mb4_general_ci'), comment='游戏人数')
    create_time = Column(TIMESTAMP)
    update_time = Column(TIMESTAMP)


class TrainCompany(Base):
    __tablename__ = 'train_company'

    id = Column(INTEGER(20), primary_key=True, comment='自增ID')
    company_name = Column(String(255, 'utf8mb4_general_ci'), nullable=False, comment='培训名称')
    company_address = Column(String(255, 'utf8mb4_general_ci'), comment='培训地址')
    create_time = Column(TIMESTAMP)
    update_time = Column(TIMESTAMP)


class User(Base):
    __tablename__ = 'user'

    id = Column(INTEGER(20), primary_key=True, comment='自增ID')
    name = Column(String(255, 'utf8mb4_general_ci'), nullable=False, comment='游戏ID')
    create_time = Column(TIMESTAMP)
    update_time = Column(TIMESTAMP)


class Vehicle(Base):
    __tablename__ = 'vehicles'

    id = Column(INTEGER(20), primary_key=True, comment='自增ID')
    name = Column(String(255, 'utf8mb4_general_ci'), nullable=False, comment='游戏ID')
    vehicles_name = Column(String(255, 'utf8mb4_general_ci'), nullable=False, comment='载具名称')
    vehicles_kills = Column(String(255, 'utf8mb4_general_ci'), comment='载具击杀数')
    vehicles_kpm = Column(String(255, 'utf8mb4_general_ci'), comment='载具每分钟击杀数')
    vehicles_destroyed = Column(String(255, 'utf8mb4_general_ci'), comment='击毁载具数量')
    create_time = Column(TIMESTAMP)
    update_time = Column(TIMESTAMP)


class Weapon(Base):
    __tablename__ = 'weapons'

    id = Column(INTEGER(20), primary_key=True, comment='自增ID')
    name = Column(String(255, 'utf8mb4_general_ci'), nullable=False, comment='游戏ID')
    weapons_name = Column(String(255, 'utf8mb4_general_ci'), nullable=False, comment='武器名称')
    weapons_kills = Column(String(255, 'utf8mb4_general_ci'), comment='武器击杀数')
    weapons_kpm = Column(String(255, 'utf8mb4_general_ci'), comment='武器每分钟击杀数')
    weapons_accuracy = Column(String(255, 'utf8mb4_general_ci'), comment='武器准度')
    weapons_headshots = Column(String(255, 'utf8mb4_general_ci'), comment='武器爆头数')
    create_time = Column(TIMESTAMP)
    update_time = Column(TIMESTAMP)
